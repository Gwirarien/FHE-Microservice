from flask import Blueprint

customerrors = Blueprint('customerrors', __name__)

from app.customerrors import error_handlers