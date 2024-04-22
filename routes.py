from flask import render_template, redirect, send_from_directory
from forms import AddProductForm, AddPostForm, FileUpload
from os import path
from models import Post, AddPost, File
from ext import app, db
from datetime import datetime


#products = [
 #       {"title": "ps4", "price": "100", "img": "images/farmacy.jpg", "id": 0},
  #      {"title": "ps5", "price": "1200", "img": "images/veterinary.jpg", "id": 1},
   #     {"title": "ps5", "price": "1200", "img": "images/it.jpg", "id": 2}
    #]
    

@app.route("/")
def home():
    programs = Post.query.all()
    posts = AddPost.query.all()
    files = File.query.all()
    
    
    role = "user"
    last_3_reversed_posts = list(reversed(posts[-3:]))  
    return render_template("index.html", programs=programs, role=role, posts=last_3_reversed_posts, files=files)



@app.route("/programs")
def programs():
    programs = Post.query.all()
    form = AddProductForm()
    if form.validate_on_submit():
        new_product = Post(name=form.name.data, price=form.price.data, img=form.img.data.filename)

        db.session.add(new_product)
        db.session.commit()

        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)
        
        return redirect("/")
    return render_template("pages/programs.html", programs=programs, form=form)


@app.route("/edit_post/<int:index>", methods=["GET", "POST"])
def edit_post(index):
    post = AddPost.query.get(index)
    form = AddPostForm(price=post.price, name=post.name, img=post.img)

    if form.validate_on_submit():
        post.name = form.name.data
        post.price = form.price.data
        post.img=form.img.data.filename

        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)

        db.session.commit()

        return redirect("/")

    return render_template("pages/add_post.html", form=form)


@app.route("/delete_post/<int:index>")
def delete_post(index):
    post = AddPost.query.get(index)

    db.session.delete(post)
    db.session.commit()
    return redirect("/")



@app.route("/view_program/<int:index>")
def view_program(index):
    product = Post.query.get(index)
    return render_template("view_program.html", product=product)


@app.route("/view_post/<int:index>")
def view_post(index):
    post = AddPost.query.get(index)
    return render_template("view_post.html", post=post)

@app.route("/news", methods=["GET", "POST"])
def about():
    posts = AddPost.query.all()
    
    form = AddPostForm()
    if form.validate_on_submit():
        new_post = AddPost(name=form.name.data, img=form.img.data.filename, date_posted=datetime.now())

        db.session.add(new_post)
        db.session.commit()

        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)
        
        return redirect("/")
    return render_template("pages/news.html", posts=posts, form=form)




@app.route("/legal_documents", methods=["GET", "POST"])
def legal_documents():
    form = FileUpload()
    if form.validate_on_submit():
        new_file = File(name=form.name.data, file=form.file.data.filename)
        db.session.add(new_file)
        db.session.commit()

        file_dir = path.join(app.root_path, "static/files", form.file.data.filename)
        form.file.data.save(file_dir)

    files = File.query.all()
    return render_template("pages/legal_documents.html", form=form, files=files)

@app.route("/delete_file/<int:index>")
def delete_file(index):
    file = File.query.get(index)
    db.session.delete(file)
    db.session.commit()
    return redirect("/legal_documents")

@app.route("/view_file/<int:index>")
def view_file(index):
    file = File.query.get(index)
    return send_from_directory(path.join(app.root_path, "static/files"), file.file)