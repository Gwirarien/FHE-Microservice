from app import db
from flask import render_template, redirect, url_for
from app.calculation.forms import CalculateForm
from app.models import Data
from flask_login import login_required, current_user
from app.calculation.key_generator import KeyGenerator
from app.calculation.matrix_encryption import MatrixEncryption
from app.calculation import calculation

def __encrypt_input_values(form):
    key_gen = KeyGenerator()
    secret_key = key_gen.generate_secret_key()
    return MatrixEncryption().encrypt_message(secret_key, form.input_value1.data), MatrixEncryption().encrypt_message(secret_key, form.input_value1.data)

@calculation.route("/calculate", methods=['GET', 'POST'])
def calculate():
    data_row = db.session.query(Data).filter(current_user.id == Data.user_id)
    data_row.delete(synchronize_session=False)
    form = CalculateForm()
    if form.validate_on_submit():
        encrypted_matrix_value1, encrypted_matrix_value2 = __encrypt_input_values(form)
        data = Data(author=current_user, input_value1=encrypted_matrix_value1, input_value2=encrypted_matrix_value2)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('calculate.html', title='Calculate', form=form)
    