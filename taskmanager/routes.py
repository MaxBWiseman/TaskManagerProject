from flask import render_template, request, redirect, url_for
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
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
    """
When a user clicks the "Add Category" button, this will use the "GET" method and render the 'add_category' template.
Once they submit the form, this will call the same function, but will check if the request
being made is a “POST“ method, which posts data somewhere, such as a database.
    """