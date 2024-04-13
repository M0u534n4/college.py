from flask import render_template, redirect
from forms import AddProductForm
from os import path
from models import Post
from ext import app, db


#products = [
 #       {"title": "ps4", "price": "100", "img": "images/farmacy.jpg", "id": 0},
  #      {"title": "ps5", "price": "1200", "img": "images/veterinary.jpg", "id": 1},
   #     {"title": "ps5", "price": "1200", "img": "images/it.jpg", "id": 2}
    #]

@app.route("/")
def home():
    products = Post.query.all()
    
    
    role = "user"
    last_3_reversed_products = list(reversed(products[-3:]))  
    return render_template("index.html", products=last_3_reversed_products, role=role)



@app.route("/programs")
def programs():
    return render_template("pages/programs.html")

@app.route("/add_post", methods=["POST", "GET"])
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        new_product = Post(name=form.name.data, price=form.price.data, img=form.img.data.filename)

        db.session.add(new_product)
        db.session.commit()

        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)
        
        return redirect("/")
    print(form.errors)
    return render_template("pages/add_product.html", form=form)

@app.route("/edit_post/<int:index>", methods=["GET", "POST"])
def edit_product(index):
    product = Post.query.get(index)
    form = AddProductForm(price=product.price, name=product.name, img=product.img)

    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.img=form.img.data.filename

        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)

        db.session.commit()

    return render_template("pages/add_product.html", form=form)


@app.route("/delete_post/<int:index>")
def delete_product(index):
    product = Post.query.get(index)

    db.session.delete(product)
    db.session.commit()
    return redirect("/")




@app.route("/view_program/<int:index>")
def test(index):
    product = Post.query.get(index)
    return render_template("test.html", product=product)

@app.route("/news")
def about():
    return render_template("pages/news.html")