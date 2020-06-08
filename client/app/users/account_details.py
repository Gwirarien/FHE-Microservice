import os
import secrets
from app import app, database
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_required, current_user
from app.users.user_forms import UpdateAccountForm
from app.users import users

def upload_picture(form_picture):
    secret_hex = secrets.token_hex(8)
    _, formatted_path = os.path.splitext(form_picture.filename)
    picture_filename = secret_hex + formatted_path
    picture_filepath = os.path.join(app.root_path, 'static/profile_pics', picture_filename)

    picture_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(picture_size)
    i.save(picture_filepath)

    return picture_filename

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    elif form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.picture.data:
            picture_file = upload_picture(form.picture.data)
            current_user.image_file = picture_file
        with app.app_context():
            database.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)
