from app import db
from flask import render_template, redirect, url_for, session, request
from app.calculation.forms import CalculateForm
from app.models import Data
from flask_login import login_required, current_user
from app.calculation.key_generator import KeyGenerator
from app.calculation.matrix_encryption import MatrixEncryption
from app.calculation.matrix_decryption import MatrixDecryption
from app.calculation import calculation
import numpy as np
import jsonpickle
import requests

def __convert_values_to_json(enc_value1, enc_value2):
    enc_input = {}
    enc_input['enc_input_value1'] = enc_value1
    enc_input['enc_input_value2'] = enc_value2
    return jsonpickle.encode(enc_input)

def __encrypt_input_values(secret_key, key_gen, form):   
    enc_value1 = MatrixEncryption().encrypt_message(secret_key, form.input_value1.data)
    enc_value2 = MatrixEncryption().encrypt_message(secret_key, form.input_value2.data)
    return __convert_values_to_json(enc_value1, enc_value2)

def __send_recieve_data(json_enc_data):
    result = requests.post("http://127.0.0.1:81", json=json_enc_data)
    return jsonpickle.decode(result.text)

def __save_data_in_database(form, output_value):
    data_row = db.session.query(Data).filter(current_user.id == Data.user_id)
    data_row.delete(synchronize_session=False)
    data = Data(author=current_user, input_value1=form.input_value1.data, input_value2=form.input_value2.data, output_value=output_value)
    db.session.add(data)
    db.session.commit()
     
@calculation.route("/calculate", methods=['GET', 'POST'])
def calculate():
    form = CalculateForm()
    if form.validate_on_submit():

        output_value = None
        while output_value == None:
            # encrypt and send to server
            key_gen = KeyGenerator()
            secret_key = key_gen.generate_secret_key()
            json_enc_data = __encrypt_input_values(secret_key, key_gen, form)
            modified_enc_data = __send_recieve_data(json_enc_data)
            enc_output_value = modified_enc_data['enc_output_value']

            # decrypt
            output_value = MatrixDecryption().decrypt_message(secret_key, enc_output_value, True)
            
        __save_data_in_database(form, output_value)
        return redirect(url_for('main.home'))
    return render_template('calculate.html', title='Calculate', form=form)

    