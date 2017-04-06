from flask_wtf import FlaskForm
from wtforms import StringField

class BasicForm(FlaskForm):
    basic_input = StringField('basic_input')
