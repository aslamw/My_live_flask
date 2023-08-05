from .. import db, ma 
import datetime

class User (db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True, unique=True)
    phone = db.Column(db.String, nullable=True, unique=True) 
    email = db.Column(db.String, nullable=True, unique=True) 
    password = db.Column(db.String, nullable=True, unique=True)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now())
    
    #Relacionamento de um para muitos (One-to-Many)
    daily = db.relationship("Daily", uselist=False, backref='user', cascade='all, delete-orphan')
    
    def __init__(self, name, phone, email, password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "phone", "email")
        
user_shema = UserSchema()
users_shema = UserSchema(many=True)
