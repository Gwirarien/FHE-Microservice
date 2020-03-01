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
import json
import requests

def __convert_values_to_json(enc_value1, enc_value2):
    enc_input = {}
    enc_input['enc_input_value1'] = str(enc_value1)
    enc_input['enc_input_value2'] = str(enc_value2)
    return json.dumps(enc_input, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def __encrypt_input_values(secret_key, key_gen, form):   
    enc_value1 = MatrixEncryption().encrypt_message(secret_key, form.input_value1.data)
    enc_value2 = MatrixEncryption().encrypt_message(secret_key, form.input_value2.data)
    return __convert_values_to_json(enc_value1, enc_value2)

def __send_recieve_data(json_enc_data):
    result = requests.post("http://127.0.0.1:81", json=json_enc_data)
    return json.loads(result.text)
     
@calculation.route("/calculate", methods=['GET', 'POST'])
def calculate():
    form = CalculateForm()
    if form.validate_on_submit():
        #encrypt
        # key_gen = KeyGenerator()
        # secret_key = key_gen.generate_secret_key()

        # json_enc_data = __encrypt_input_values(secret_key, key_gen, form)
        # modified_enc_data = __send_recieve_data(json_enc_data)
        # enc_input_value1 = modified_enc_data['enc_input_value1']
        # enc_input_value2 = modified_enc_data['enc_input_value2']

        # enc_input_value1 = np.asarray(enc_input_value1)
        # enc_input_value2 = np.asarray(enc_input_value2)

        # decrypt 
        # input_value1 = MatrixDecryption().decrypt_message(secret_key, enc_input_value1, True)
        # input_value2 = MatrixDecryption().decrypt_message(secret_key, enc_input_value2, True)
        


        # TODO: delete database integration for the calculation
        data_row = db.session.query(Data).filter(current_user.id == Data.user_id)
        data_row.delete(synchronize_session=False)

        input = {}
        input['input1'] = form.input_value1.data
        input['input2'] = form.input_value2.data
        json_data = json.dumps(input, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        result = requests.post("http://127.0.0.1:81", json=json_data)
        data = json.loads(result.text)

        data = Data(author=current_user, input_value1=data['input1'], input_value2=data['input2'])
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('calculate.html', title='Calculate', form=form)

    