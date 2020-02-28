from flask import url_for, redirect
from flask_login import logout_user
from app.users import users

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))