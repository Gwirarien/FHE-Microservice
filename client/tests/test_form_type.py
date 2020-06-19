import pytest
from flask import Flask
from app.calculation.calculator_forms import CalculateForm
from app.users.user_forms import RegistrationForm, LoginForm
from app.config import DevelopmentConfig

import warnings
warnings.simplefilter("ignore", category=PendingDeprecationWarning)

def init_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.app_context().push()
    return app

def test_calculator_form_type():
    app = init_app()
    with app.test_request_context('/'):
        calculate_form = CalculateForm()
        assert type(calculate_form) is CalculateForm

def test_login_form_type():
    app = init_app()
    with app.test_request_context('/'):
        login_form = LoginForm()
        assert type(login_form) is LoginForm

def test_register_form_type():
    app = init_app()
    with app.test_request_context('/'):
        register_form = RegistrationForm()
        assert type(register_form) is RegistrationForm


