from flask import render_template
from app.main import main

@main.route("/about")
def about():
    return render_template('about.html', title='About')