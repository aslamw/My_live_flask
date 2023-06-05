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
    date_delete = db.Column(db.DateTime)
    
    #Relacionamento de um para muitos (One-to-Many)
    daily = db.relationship("Daily", backref="User", lazy=True)
    
    def __init__(self, name, phone, email, password, date_delete=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.date_delete = date_delete
        
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "phone", "email", "password")
        
user_shema = UserSchema()
users_shema = UserSchema(many=True)
