from app import app, db
from flask import render_template
from app.forms import CalculateForm
from app.models import Data
from flask_login import login_required

@app.route("/calculate", methods=['GET', 'POST'])
def calculate():
    form = CalculateForm()
    # if form.validate_on_submit():
    '''Insert in the database the data from the from, after being encrypted'''
    # data = Data(username=form.username.data, email=form.email.data, password=hashed_password) 
    return render_template('calculate.html', title='Calculate', form=form)
    