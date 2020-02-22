from app import app, db
from flask import render_template, redirect, url_for
from app.forms import CalculateForm
from app.models import Data
from flask_login import login_required, current_user

@app.route("/calculate", methods=['GET', 'POST'])
def calculate():
    data_row = db.session.query(Data).filter(current_user.id == Data.user_id)
    data_row.delete(synchronize_session=False)
    form = CalculateForm()
    if form.validate_on_submit():
        data = Data(author=current_user, input_value1=form.input_value1.data, input_value2=form.input_value2.data)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('calculate.html', title='Calculate', form=form)
    