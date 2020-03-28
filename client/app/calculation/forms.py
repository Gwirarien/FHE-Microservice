from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange

class CalculateForm(FlaskForm):
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
    age = IntegerField('Age', validators=[NumberRange(min=20, message='Age must be bigger than 20!'), DataRequired()])
    total_cholesterol = FloatField('Total cholesterol (mg/dL)', validators=[NumberRange(min=50, max=350, message='Value not allowed'), DataRequired()])
    smoker = SelectField('Smoker', choices=[('no', 'No'), ('yes', 'Yes')])
    hdl_cholesterol = FloatField('HDL cholesterol (mg/dL)', validators=[NumberRange(min=0, max=100, message='Value not allowed'), DataRequired()])
    systolic_blood_pressure = FloatField('Systolic blood pressure (mm Hg)', validators=[NumberRange(min=70, max=250, message='Value not allowed'), DataRequired()])
    submit_values = SubmitField('Calculate!')
