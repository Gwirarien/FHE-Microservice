import pytest
import app
from flask import Flask

import warnings
warnings.simplefilter("ignore", category=PendingDeprecationWarning)

def test_wrong_route():
    test_app = app.process()
    with test_app.test_client() as client:
        response = client.get('/process')
        assert response.status_code == 200

def test_wrong_route():
    test_app = Flask(__name__)
    with test_app.test_client() as client:
        response = client.get('/asad')
        assert response.status_code == 404