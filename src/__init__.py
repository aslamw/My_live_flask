from flask import Flask
from flask_cors import CORS
from .models import db,ma
from flask_migrate import Migrate
from dotenv import load_dotenv
from .routes import api_user

import os

load_dotenv()

banco = os.getenv("BANCO")
data_base = os.getenv("DATA_BASE")

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = f"{banco}:///{data_base}"
app.config["SQLALCHEMY_BINDS"] = {
    "in_memory": "sqlite:///:memory:"
}

db.init_app(app)
ma.init_app(app)
mi = Migrate(app, db)

#table
from .models import User, Daily

#CRUD
#from .models import create_user,get_user

app.register_blueprint(api_user)
