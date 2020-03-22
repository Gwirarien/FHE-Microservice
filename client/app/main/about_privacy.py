from flask import render_template
from app.main import main

@main.route("/about_privacy")
def about_privacy():
    return render_template('about_privacy.html', title='About Privacy')