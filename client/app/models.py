from app import db, login_manager
from flask_login import UserMixin
import sqlalchemy.types as types
import numpy as np

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    data = db.relationship('Data', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Data(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)
    input_value1 = db.Column(db.Float)
    input_value2 = db.Column(db.Float)
    output_value = db.Column(db.Float)

    def __repr__(self):
        return f"Data('{self.user_id}', '{self.input_value1}', '{self.input_value2}', '{self.output_value}')"