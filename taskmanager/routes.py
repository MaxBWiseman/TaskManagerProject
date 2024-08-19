from flask import render_template, request
from taskmanager import app, db
from taskmanager.models import Category, Task



@app.route("/")
def home():# resieves the home() function from clicking nav links
    return render_template("tasks.html")
# The home route is the default route that renders the tasks.html template.
# this page will be displayed always when the user visits the website first.

@app.route("/categories")
def categories():# resieves the categories() function from clicking nav links
    return render_template("categories.html")

@app.route("/add_category", methods=["GET", "POST"])# when user submits the form, the data is sent to the database
def add_category():# resieves the add_category() function from clicking nav links
    if request.method == "POST":
        category = Category(name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
    return render_template("add_category.html")