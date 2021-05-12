from db import db

class Coche(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  Marca = db.Column(db.String(255))
  tipo = db.Column(db.String(255))
  conductor = db.Column(db.String(255))

  def __str__(self):
    return (
      f'Id: {self.id} '
      f'Marca: {self.marca} '
      f'Tipo: {self.tipo} '
      f'Conductor: {self.conductor} '
    )

class Persona(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  nombre = db.Column(db.String(255))
  apellido = db.Column(db.String(255))
  email = db.Column(db.String(255))

  def __str__(self):
    return (
      f'Id: {self.id} '
      f'Nombre: {self.nombre} '
      f'Apellido: {self.apellido} '
      f'Email: {self.email} '
    )