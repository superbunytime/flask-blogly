from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

"""Models for Blogly."""

class User(db.Model):
    """User"""
    __tablename__ = "Users"

    id = db.Column(db.Integer,
    primary_key=True,
    autoincrement=True)

    first_name = db.Column(db.String(50),
    nullable=False,
    unique=True)

    last_name = db.Column(db.String(50),
    nullable=False,
    unique=True)

    image_url = db.Column(db.String(1000),
    nullable=False,
    unique=True)