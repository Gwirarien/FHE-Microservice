from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import DataRequired

class CalculateForm(FlaskForm):
    input_value1 = FloatField('Input value 1', validators=[DataRequired()])
    input_value2 = FloatField('Input value 2', validators=[DataRequired()])
    submit_values = SubmitField('Calculate!')