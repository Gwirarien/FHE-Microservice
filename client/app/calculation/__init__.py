from flask import Blueprint

calculation = Blueprint('calculation', __name__)

from app.calculation import calculate
