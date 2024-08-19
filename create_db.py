from taskmanager import app, db

with app.app_context():
    db.create_all()
    
# This script creates the database tables by importing the app and db objects from the taskmanager
# package and calling the create_all() method on the db object within the app context. The app context
# is necessary to ensure that the app and db objects are properly initialized before creating the tables.
# This script can be run from the command line using the following command: python create_db.py