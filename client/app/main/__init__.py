from flask import Blueprint

main = Blueprint('main', __name__)

from app.main import home
from app.main import about_privacy
