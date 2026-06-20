from flask import Flask, render_template, request, redirect, session
from database import db, Product
import os

app = Flask(**name**)
app.secret_key = "digitalaestheticsecret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///deals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db.init_app(app)

with app.app_context():
db.create_all()

# LOGIN

@app.route("/login", methods=["GET", "POST"])
def login():

```
if request.method == "POST":

    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "12345":

        session["admin"] = True
        return redirect("/admin")

return render_template("login.html")
```

# LOGOUT

@app.route("/logout")
def logout():

```
session.pop("admin", None)
return redirect("/login")
```

# HOME PAGE

@app.route("/")
def home():

```
search = request.args.get("search")
category = request.args.get("category")

products = Product.query

if search:
    products = products.filter(
        Product.title.contains(search)
    )

if category:
    products = products.filter_by(
        category=category
    )

products = products.all()

return render_template(
    "index.html",
    products=products,
    search=search,
    category=category
)
```

# ADMIN PAGE

@app.route("/admin")
def admin():

```
if "admin" not in session:
    return redirect("/login")

products = Product.query.all()

return render_template(
    "admin.html",
    products=products
)
```

# ADD PRODUCT

@app.route("/add-product", methods=["GET", "POST"])
def add_product():

```
if "admin" not in session:
    return redirect("/login")

if request.method == "POST":

    title = request.form["title"]
    price = request.form["price"]
    category = request.form["category"]
    affiliate_link = request.form["affiliate_link"]

    image = request.files["image"]

    if image and image.filename:

        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        filename = image.filename

        image.save(
            os.path.join(
                app.config['UPLOAD_FOLDER'],
                filename
            )
        )

        product = Product(
            title=title,
            price=price,
            category=category,
            image=filename,
            affiliate_link=affiliate_link
        )

        db.session.add(product)
        db.session.commit()

    return redirect("/admin")

return render_template("add_product.html")
```

# EDIT PRODUCT

@app.route("/edit/[int:id](int:id)", methods=["GET", "POST"])
def edit_product(id):

```
if "admin" not in session:
    return redirect("/login")

product = Product.query.get_or_404(id)

if request.method == "POST":

    product.title = request.form["title"]
    product.price = request.form["price"]
    product.category = request.form["category"]
    product.affiliate_link = request.form["affiliate_link"]

    image = request.files["image"]

    if image and image.filename:

        filename = image.filename

        image.save(
            os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )
        )

        product.image = filename

    db.session.commit()

    return redirect("/admin")

return render_template(
    "edit_product.html",
    product=product
)
```

# DELETE PRODUCT

@app.route("/delete/[int:id](int:id)")
def delete_product(id):

```
if "admin" not in session:
    return redirect("/login")

product = Product.query.get_or_404(id)

db.session.delete(product)
db.session.commit()

return redirect("/admin")
```

if **name** == "**main**":
app.run(debug=True)
