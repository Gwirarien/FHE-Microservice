from app import app, db, bcrypt
from flask import render_template, url_for, flash, redirect
from app.forms import RegistrationForm
from app.models import User, Data
from flask_login import current_user

def create_data_table(user):
    data = Data(author=user, input_value1=0, input_value2=0)
    db.session.add(data)
    db.session.commit()

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        create_data_table(user)
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)