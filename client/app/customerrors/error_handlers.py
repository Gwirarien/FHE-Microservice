from flask import render_template
from app.customerrors import customerrors

@customerrors.app_errorhandler(403)
def error_403(error):
    return render_template('custom_errors/403_response.html'), 403

@customerrors.app_errorhandler(404)
def error_404(error):
    return render_template('custom_errors/404_response.html'), 404

@customerrors.app_errorhandler(500)
def error_500(error):
    return render_template('custom_errors/500_response.html'), 500