from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

#User
from .user.table import User, user_shema
from .user.CRUD import UserCRUD


from .daily.table import Daily, daily_shema, dailys_shema
from .daily.CRUD import CRUDaily