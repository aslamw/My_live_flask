from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from .models import db, ma
from .routes import api_user, api_daily


import os, datetime

load_dotenv()


def create_app(data_base):
    app = Flask(__name__)

    CORS(app)

    key = os.getenv("KEY")

    app.config["JWT_SECRET_KEY"] = key
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=1)

    jwt = JWTManager(app)

    banco = os.getenv("BANCO")
    # data_base = os.getenv("DATA_BASE")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"{banco}:///{data_base}"

    db.init_app(app)
    ma.init_app(app)
    # table

    app.register_blueprint(api_user)
    app.register_blueprint(api_daily)

    return app
