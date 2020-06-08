from flask import render_template, redirect, url_for
from flask_login import current_user
from app.main import main

@main.route("/")
@main.route("/home")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('main.forum'))
    return render_template('home.html', isHome=True)