from app import db, bcrypt
from flask import render_template, url_for, flash, redirect
from flask_login import current_user
from app.users.forms import RegistrationForm
from app.models import User
from app.users import users

# TODO: delete/initialize params with column data type values
def create_data_table(user):
    data = Data(author=user, input_value1=0, input_value2=0)
    db.session.add(data)
    db.session.commit()

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        #create_data_table(user)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)