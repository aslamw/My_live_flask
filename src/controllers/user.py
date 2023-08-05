from flask import jsonify
from ..models import UserCRUD, user_shema
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from flask_jwt_extended import create_access_token
import re
import datetime as dt

#fomat valid email
F_email = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
class ControllerUser:
    

    @staticmethod
    def register_user(data):
        global F_email
        
        if not data['name'] or not data['phone'] or not data['password'] or not data['email']:
            return jsonify({"message":"All fields are mandatory"}),400
        
        if not re.search(r'^[A-Za-z\s]+$', data["name"]):
            return jsonify({"message":"name invalid"}),400
        
        if not F_email.match(data['email']):
            return jsonify({"message":"E-mail invalid"}),400
        
        if UserCRUD.get_email(data.get("email")) or UserCRUD.get_phone(data.get("phone")):
            return jsonify({"message":"E-mail or Phone exist"}),400
        
        data["password"] = generate_password_hash(data['password'])
        
        state = UserCRUD.create_user(data)
        
        if state:
            return jsonify({"menssage":"success create"}),201
        
        else: jsonify({"menssage":"error"}),400
    
    @staticmethod  
    def login(data):
        global F_email
        if data.get("email") is None or data.get("password") is None:
            return jsonify({"menssage":"All fields are mandatory"}),400
        
        if not F_email.match(data['email']):
            return jsonify({"menssage":"E-mail invalid"}),400
        
        user = UserCRUD.get_email(data.get("email"))
        
        if not user:
            return jsonify({"message":"user not exist"})
        
        if not check_password_hash(user.password, data["password"]):
            return jsonify('invalid password'),401
        
        access_token = create_access_token(identity=user.id, expires_delta=dt.timedelta(hours=1))
        
        
        return jsonify({"token":access_token}),200
    
    @staticmethod
    def get_data_user(id):
        
        user = UserCRUD.get_id(id)
        
        if not user:
            return jsonify({"message":"User not exist"}),400
        
        return jsonify({"user": user_shema.dump(user)}),200
    
    @staticmethod
    def update_user(id,data):
        user = UserCRUD.get_id(id)
        
        if not user:
            return jsonify({"message":"User not exist"}),400
        
        if data.get("name")is not None:
            if not re.search(r'^[A-Za-z\s]+$', data["name"]):
                return jsonify({"message":"name invalid"}),400
            
        if data.get("email" )is not None:
            if not F_email.match(data['email']):
                return jsonify({"message":"E-mail invalid"}),400
            email = UserCRUD.get_email(data.get("email"))
        
            if email:
                return jsonify({"message":"email exist"})
            
        if data.get("password")is not None:
            data["password"] = generate_password_hash(data['password'])
        
        return jsonify({"user": UserCRUD.update_user(data,user)}),200
        
    
    @staticmethod
    def delete_user(id):
        
        user = UserCRUD.get_id(id)
        UserCRUD.delete_user(user)
        
        if not user:
            return jsonify({"message":"User not exist"}),400
        
        return jsonify({"user": "successfully deleted"}),200
        
        