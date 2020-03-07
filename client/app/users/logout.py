from flask import url_for, redirect, session
from flask_login import logout_user
from app.users import users

@users.route("/logout")
def logout():
    logout_user()
    session.pop('values', None)
    return redirect(url_for('main.home'))