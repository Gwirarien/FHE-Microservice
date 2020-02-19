from app import app
from flask import render_template
from flask_login import login_required

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')