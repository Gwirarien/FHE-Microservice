from flask import Blueprint

users = Blueprint('users', __name__)

from app.users import login
from app.users import register
from app.users import account
from app.users import logout