from flask_migrate import Migrate
from db import db
from app import app

#configurar flask-migrate
migrate = Migrate()
migrate.init_app(app, db)