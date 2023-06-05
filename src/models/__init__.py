from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

#User
from .user.table import User
from .user.CRUD import get_user, create_user, exist_user


from .daily.table import Daily