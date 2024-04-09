from flask import Flask, render_template
from forms import AddProductForm
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
    
    last_three_items = products[-3:]
    role = "user"

    return render_template("index.html", products=products, role=role, last_three_items=last_three_items)

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
        form.img.data.save(f"{app.root_path}\\static\\{form.img.data.filename}")
        products.append(new_product)
    return render_template("pages/add_product.html", form=form)


@app.route("/news")
def about():
    return render_template("pages/news.html")

@app.route("/test/<int:index>")
def test(index):
    
    
    return render_template("test.html", products=products[index])

app.run(debug=True)