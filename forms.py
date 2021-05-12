from wtforms.fields.simple import SubmitField
from wtforms.fields.core import StringField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class PersonaForm(FlaskForm):
  nombre = StringField('Nombre', validators = [DataRequired()])
  apellido = StringField('Apellido')
  email = StringField('Email', validators=[DataRequired()])
  enviar = SubmitField('Enviar')