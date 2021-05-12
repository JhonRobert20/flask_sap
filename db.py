from flask_sqlalchemy import SQLAlchemy
from app import app

#Configuración de la base de datos
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'flask_sap_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inicialización del objeto db a la sqlalchemy
db = SQLAlchemy(app)

from models import Persona
from forms import PersonaForm