import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy, Model
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
from core.entity.custom_meta import NoNameMeta

environment = os.getenv('BANKS_ENV')
if environment is None or not environment:
    environment = 'local'
if environment == 'local':
    load_dotenv("./resources/.env")
else:
    load_dotenv("./resources/.env." + environment)
DEBUG = True

app = Flask(__name__)
SECRET_KEY = os.getenv("SECRET_KEY")

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_PASS = os.getenv("POSTGRES_PASS")
POSTGRES_USER = os.getenv("POSTGRES_USER")

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://" \
                                        f"{POSTGRES_USER}:" \
                                        f"{POSTGRES_PASS}@" \
                                        f"{POSTGRES_HOST}:" \
                                        f"{POSTGRES_PORT}/" \
                                        f"{POSTGRES_DB}"
app.config.from_object(__name__)
Base = declarative_base(
    cls=Model, metaclass=NoNameMeta, name='Model')
db = SQLAlchemy(app=app, model_class=Base)
migrate = Migrate(app, db)

from core.entity.banks_entity import BankEntity

db.create_all()

CORS(app, resources={r'/*': {'origins': '*'}})

from core.controllers import banks_controller
