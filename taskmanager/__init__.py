import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):#as the env.py file is in the .gitignore file, it will not be pushed to github
    import env #Therefore, the env.py file will not be available on the deployed site
    #This is why the if statement is used to check if the env.py file exists
    
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes