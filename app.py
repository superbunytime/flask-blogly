"""Blogly application."""

from flask import Flask
from models import db, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route('/')
def show_base():
    return render_template('base.html')

@app.route('/users' methods =['GET'])
def users():
    # unfinished route
    return render_template('users.html')