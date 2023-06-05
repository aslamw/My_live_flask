from sqlalchemy.orm import Session
from sqlalchemy import exists, inspect
from .table import User, user_shema, users_shema
from .. import db

def get_user(id):
    
    data = User.query.filter(User.id == id).one()
    
    if not data:
        return False
    
    db.session.commit()
    return user_shema.dump(data)

def exist_user(data):
    
    if len(list((key := data.key()))) > 1 or key not in ['email','id','phone']:
        return False
    
    match key:
        case 'id':
            user = User.query.filter(User.id == data[key]).one()
        case 'phone':
            user = User.query.filter(User.phone == data[key]).one()
        case 'email':
            user = User.query.filter(User.email == data[key]).one()
        case _:
            return False
    if not user:
        return False
    
    db.session.commit()
    return True


def create_user(data):
    print(data)
    data = User(
        data["name"],
        data["phone"],
        data["email"],
        data["password"]
    )
    
    db.session.add_all([data])
    db.session.commit()
    
    return user_shema.dump(data)
    
    
