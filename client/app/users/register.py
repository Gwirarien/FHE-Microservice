from app import app, database, bcrypt
from flask import render_template, url_for, flash, redirect
from flask_login import current_user
from app.users.user_forms import RegistrationForm
from app.models import User
from app.users import users

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        with app.app_context():
            database.session.add(user)
            database.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)