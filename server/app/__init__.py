from flask import Flask, request
import numpy as np
import jsonpickle 

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def process():      
    # decode data
    received_data = jsonpickle.decode(request.data)
    received_data = jsonpickle.decode(received_data)
    
    # perform computation
    enc_input_value1 = received_data['enc_value1']
    enc_input_value2 = received_data['enc_value2']

    enc_output = {}
    enc_output['enc_output_value'] = np.add(enc_input_value1, enc_input_value2)

    # send back data as json
    return jsonpickle.encode(enc_output)
