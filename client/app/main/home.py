from app import db
from flask import render_template, request, session
from flask_login import current_user
from sqlalchemy.sql import text
from app.main import main
import jsonpickle

@main.route("/")
@main.route("/home")
def home():
    if current_user.is_authenticated:
        try:
            values = session['values']
            return render_template('home.html', values=values)
        except:
            values = None
            
    return render_template('home.html')