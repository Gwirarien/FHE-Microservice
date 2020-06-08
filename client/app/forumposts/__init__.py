from flask import Blueprint

posts = Blueprint('posts', __name__)

from app.forumposts import view_post
from app.forumposts import create_post
from app.forumposts import update_post
from app.forumposts import delete_post