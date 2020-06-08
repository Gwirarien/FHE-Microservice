from app import database
from flask import render_template
from app.calculation import calculation
from app.calculation.calculator_forms import CalculateForm
from app.calculation.key_generator import KeyGenerator
from app.calculation.matrix_encryption import MatrixEncryption
from app.calculation.matrix_decryption import MatrixDecryption
from app.calculation.framingham import Framingham
import jsonpickle
import requests

def __convert_values_to_json(enc_values):
    enc_input = {}
    index = 1
    for i in enc_values:   
        enc_input['enc_value{}'.format(index)] = i
        index = index + 1
    return jsonpickle.encode(enc_input)

def __encrypt_input_values(secret_key, key_gen, score):   
    enc_values = []
    for i in range(len(score)):
        enc_values.append(MatrixEncryption().encrypt_message(secret_key, score[i]))
    return __convert_values_to_json(enc_values)

def __send_receive_data(json_enc_data):
    result = requests.post("http://127.0.0.1:5001/", json=json_enc_data)
    return jsonpickle.decode(result.text)
 
@calculation.route("/calculate", methods=['GET', 'POST'])
def calculate():
    form = CalculateForm()
    if form.validate_on_submit():

        # map score accordingly to the Framingham formula
        score = Framingham().convert_values_to_score(form)

        output_value = None        
        while output_value == None:
            # encrypt and send to server
            key_gen = KeyGenerator()
            secret_key = key_gen.generate_secret_key()
            json_enc_data = __encrypt_input_values(secret_key, key_gen, score)
            modified_enc_data = __send_receive_data(json_enc_data)
            enc_output_value = modified_enc_data['enc_output_value']

            # decrypt 
            output_value = MatrixDecryption().decrypt_message(secret_key, enc_output_value, True)
        risk = Framingham().convert_score_to_risk(form, output_value)
        return render_template('calculate.html', title='Calculate', form=form, risk=risk)
    return render_template('calculate.html', title='Calculate', form=form)

    