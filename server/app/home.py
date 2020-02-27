from app import app, db
from flask import render_template
from app.models import User, Data
from flask_login import current_user
from sqlalchemy.sql import text
import sqlitis

@app.route("/")
@app.route("/home")
def home():
    data = 0
    if current_user.is_authenticated:
        data = db.session.query(Data).join(User).filter(User.id == current_user.id).first()

        #print(data.input_value1)
        #print(data.input_value2)

    return render_template('home.html', data=data)