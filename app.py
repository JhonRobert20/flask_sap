from flask import Flask
app = Flask(__name__)

from migrates import *
from funciones import *

app.config['SECRET_KEY'] = 'llave_secreta'

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
  return funcion_inicio()

@app.route('/ver/<int:id>')
def ver_detalles(id):
  return funcion_ver_detalles(id)

@app.route('/agregar', methods = ["GET", "POST"])
def agregar():
  return funcion_agregar()

@app.route('/editar/<int:id>', methods = ["GET", "POST"])
def editar(id):
  return funcion_editar(id)

@app.route('/eliminar/<int:id>')
def eliminar(id):
  return funcion_eliminar(id)