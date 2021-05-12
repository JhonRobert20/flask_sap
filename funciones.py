from flask.helpers import url_for
from werkzeug.utils import redirect
from forms import PersonaForm
from db import Persona
from db import db
from flask import render_template, request, url_for
from werkzeug.utils import redirect
from app import app

def funcion_inicio():
  #Listado de personas
  personas = Persona.query.order_by('id')
  total_personas = Persona.query.count()

  return render_template('index.html', personas = personas, total_personas = total_personas)

def funcion_ver_detalles(id):
  persona = Persona.query.get_or_404(id)
  return render_template('detalle.html', persona = persona)

def funcion_agregar():
  persona = Persona()
  personaForm = PersonaForm(obj=persona)
  if request.method == "POST":
    if personaForm.validate_on_submit():
      personaForm.populate_obj(persona)
      db.session.add(persona)
      db.session.commit()
      return redirect(url_for('inicio'))

  return render_template('agregar.html', forma = personaForm)

def funcion_editar(id):
  persona = Persona.query.get_or_404(id)
  personaForma = PersonaForm(obj = persona)
  if request.method == "POST":
    if personaForma.validate_on_submit():
      personaForma.populate_obj(persona)
      db.session.commit()
      return redirect(url_for('inicio'))

  return render_template('editar.html', forma = personaForma)

def funcion_eliminar(id):
  persona = Persona.query.get_or_404(id)
  app.logger.debug(f'Persona: {persona}')
  db.session.delete(persona)
  db.session.commit()
  return redirect(url_for('inicio'))