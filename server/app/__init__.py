from flask import Flask, request
import numpy as np
import json

app = Flask(__name__)

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

@app.route("/", methods=['GET', 'POST'])
def process():      
    received_data = json.loads(request.data)
    
    # save the json for debug purposes
    writeToJSONFile('./', 'dummy', received_data)
    return received_data
