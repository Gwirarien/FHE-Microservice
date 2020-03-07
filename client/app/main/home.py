from app import db
from flask import render_template
from app.models import User, Data
from flask_login import current_user
from sqlalchemy.sql import text
from app.main import main

@main.route("/")
@main.route("/home")
def home():
    data = 0
    if current_user.is_authenticated:
        data = db.session.query(Data).join(User).filter(User.id == current_user.id).first()
    return render_template('home.html', data=data)