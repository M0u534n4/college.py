from flask import Flask, render_template, redirect
from forms import AddProductForm
from os import path
from datetime import datetime
app = Flask(__name__)
app.config["SECRET_KEY"] = "gu[xi=71uW_Y3:?uiH}^d1R.l<UQnV.o8^0w}o7V9a4rQ#I!"

products = [
        {"title": "ps4", "price": "100", "img": "images/farmacy.jpg", "id": 0},
        {"title": "ps5", "price": "1200", "img": "images/veterinary.jpg", "id": 1},
        {"title": "ps5", "price": "1200", "img": "images/it.jpg", "id": 2}
    ]

@app.route("/")
def home():
    print(f"{app.root_path}\\static\\images")
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    
    role = "user"
    last_3_reversed_products = list(reversed(products[-3:]))  
    return render_template("index.html", products=last_3_reversed_products, role=role, current_date=current_date)



@app.route("/programs")
def programs():
    return render_template("pages/programs.html")

@app.route("/add_product", methods=["POST", "GET"])
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        new_product = {
            "title": form.name.data,
            "price": form.price.data,
            "img": form.img.data.filename,
            "id": len(products)
        }
        file_dir = path.join(app.root_path, "static", form.img.data.filename)
        form.img.data.save(file_dir)
        products.append(new_product)
        
        return redirect("/")
    print(form.errors)
    return render_template("pages/add_product.html", form=form)


@app.route("/news")
def about():
    return render_template("pages/news.html")

@app.route("/test/<int:index>")
def test(index):
    
    
    return render_template("test.html", products=products[index])

app.run(debug=True)