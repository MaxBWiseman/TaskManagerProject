from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task



@app.route("/")
def home():
    return render_template("tasks.html")
# The home route is the default route that renders the tasks.html template.
# this page will be displayed always when the user visits the website first.