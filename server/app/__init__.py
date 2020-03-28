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
    sum_value = 0
    for i in range(1, 5):   
        sum_value = np.add(received_data['enc_value{}'.format(i)], sum_value)

    enc_output = {}
    enc_output['enc_output_value'] = sum_value

    # send back data as json
    return jsonpickle.encode(enc_output)
