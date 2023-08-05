from .table import User, user_shema, users_shema
from .. import db


class UserCRUD:
    
    @staticmethod
    def get_email(data):
        
        user = User.query.filter(User.email == data).first()
        
        if user is None:
            return False
        
        return user
    
    @staticmethod
    def get_phone(data):
        
        user = User.query.filter(User.phone == data).first()
        
        if user is None:
            return False
        
        return user
    
    @staticmethod
    def get_id(data):
        
        user = User.query.filter(User.id == data).first()
        
        if user is None:
            return False
        
        return user

    @staticmethod
    def create_user(data):
        data = User(
            data["name"],
            data["phone"],
            data["email"],
            data["password"]
        )

        db.session.add_all([data])
        db.session.commit()

        return user_shema.dump(data)
    
    @staticmethod
    def update_user(data, user):     
        if data.get("name")is not None:
            user.name = data["name"]
            
        if data.get("email")is not None:
            user.name = data["email"]
            
        if data.get("phone")is not None:
            user.name = data["phone"]
            
        if data.get("password")is not None:
            user.name = data["password"]
            
        db.session.commit()
        
        return user_shema.dump(user)
    
    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()
        
        
