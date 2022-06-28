# Creating the tables 
from app import db

class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String, nullable =False)
    complete = db.Column(db.Boolean, nullable = False)