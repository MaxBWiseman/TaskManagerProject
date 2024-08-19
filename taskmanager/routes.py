from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task



@app.route("/")
def home():# calls the home() function from clicking nav links
    return render_template("tasks.html")
# The home route is the default route that renders the tasks.html template.
# this page will be displayed always when the user visits the website first.

@app.route("/categories")
def categories():# calls the categories() function from clicking nav links
    categories = list(Category.query.order_by(Category.category_name).all())
    #Whenever we call this function by clicking the navbar link for Categories, it will query
    #the database and retrieve all records from this table, then sort them by the category name.
    return render_template("categories.html", categories=categories)
#The first declaration of 'categories' is the variable name that we can now use within the HTML template.
#The second 'categories', which is now a list(), is the variable defined within our function


@app.route("/add_category", methods=["GET", "POST"])# when user submits the form, the data is sent to the database
def add_category():# calls the add_category() function from clicking nav links
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
    
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)
