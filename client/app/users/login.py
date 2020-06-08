from app import database, bcrypt
from flask import render_template, url_for, flash, redirect
from flask_login import current_user, login_user
from app.users.user_forms import LoginForm
from app.models import User
from app.users import users

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Login failed. Please check your input data', 'danger')
    return render_template('login.html', title='Login', form=login_form)
