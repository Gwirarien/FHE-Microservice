from app import db, login_manager
from flask_login import UserMixin
import sqlalchemy.types as types
from pyquaternion import Quaternion
import numpy as np

class EncryptedValue(types.UserDefinedType):
    def __init__(self, *args):
        self._args = args

    def get_col_spec(self, **kw):
        return "input_value1(%s)"

    def bind_processor(self, dialect):
        def process(value):
            return value
        return process

    # def result_processor(self, dialect, coltype):
    #     def process(value):
    #         print(value)
    #         return value
    #     return process

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
    input_value1 = db.Column(EncryptedValue)
    input_value2 = db.Column(EncryptedValue)
    enc_solution_matrix = db.Column(EncryptedValue)

    def __repr__(self):
        return f"Data('{self.input_value1}', '{self.input_value2}')"