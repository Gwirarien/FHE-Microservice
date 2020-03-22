from app import db
from flask import render_template, redirect, url_for, session, request
from app.calculation.forms import CalculateForm
from flask_login import login_required, current_user
from app.calculation.key_generator import KeyGenerator
from app.calculation.matrix_encryption import MatrixEncryption
from app.calculation.matrix_decryption import MatrixDecryption
from app.calculation import calculation
import numpy as np
import jsonpickle
import requests

def __convert_values_to_json(enc_values):
    enc_input = {}
    index = 1
    for i in enc_values:   
        enc_input['enc_value{}'.format(index)] = i
        index = index + 1
    return jsonpickle.encode(enc_input)

def __encrypt_input_values(secret_key, key_gen, form):   
    enc_value1 = MatrixEncryption().encrypt_message(secret_key, form.input_value1.data)
    enc_value2 = MatrixEncryption().encrypt_message(secret_key, form.input_value2.data)
    enc_values = [enc_value1, enc_value2]
    return __convert_values_to_json(enc_values)

def __send_receive_data(json_enc_data):
    result = requests.post("https://homomorphic-encryption-server.herokuapp.com/", json=json_enc_data)
    return jsonpickle.decode(result.text)
 
@calculation.route("/calculate", methods=['GET', 'POST'])
def calculate():
    form = CalculateForm()
    session['values'] = 0
    if form.validate_on_submit():

        output_value = None
        while output_value == None: #Workaround to display values
            # encrypt and send to server
            key_gen = KeyGenerator()
            secret_key = key_gen.generate_secret_key()
            json_enc_data = __encrypt_input_values(secret_key, key_gen, form)
            modified_enc_data = __send_receive_data(json_enc_data)
            enc_output_value = modified_enc_data['enc_output_value']

            # decrypt 
            output_value = MatrixDecryption().decrypt_message(secret_key, enc_output_value, True)
            
            # Display correct values - temporary code
            sum_values = form.input_value1.data + form.input_value2.data            
            if output_value != sum_values:
                continue

        values = [form.input_value1.data, form.input_value2.data, output_value]
        return render_template('calculate.html', title='Calculate', form=form, values=values)
    return render_template('calculate.html', title='Calculate', form=form)

    