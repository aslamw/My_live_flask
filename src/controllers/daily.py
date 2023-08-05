from ..models import CRUDaily, UserCRUD, dailys_shema, user_shema, daily_shema
from flask import jsonify
from flask_jwt_extended import create_access_token


class ControllersDaily:
    
    def register(id,text):
        
        user = UserCRUD.get_id(id)
        if not user:
            return jsonify({'message':'user not exist'}),400
        
        data = CRUDaily.registe_text(id, text)
        
        return jsonify(data),200
    
    def get_all(id):
        
        user = UserCRUD.get_id(id)
        if not user:
            return jsonify({'message':'user not exist'}),400
        
        data = CRUDaily.get_all_id(id)
        
        return jsonify(data),200
    
    def get_annotation(id, id_user):
        user = UserCRUD.get_id(id_user)
        if not user:
            return jsonify({'message':'user not exist'}),400
        
        daily = CRUDaily.get_id(id,id_user)
        if not daily:
            return jsonify({'message':'annotation not exist'}),400
        
        return jsonify(daily_shema.dump(daily)),200
        
        
    def update(id_user,id, text):
        
        user = UserCRUD.get_id(id_user)
        if not user:
            return jsonify({'message':'user not exist'}),400
        
        daily = CRUDaily.get_id(id,id_user)
        if not daily:
            return jsonify({'message':'annotation not exist'}),400
        
        
        data = CRUDaily.update(daily, text)
        
        return jsonify(data),200
    
    def delete(id,id_user):
        
        user = UserCRUD.get_id(id_user)
        if not user:
            return jsonify({'message':'user not exist'}),400
        
        daily = CRUDaily.get_id(id,id_user)
        if not daily:
            return jsonify({'message':'annotation not exist'}),400
        
        
        CRUDaily.delete(daily)
        
        return jsonify({"message":"annotation deleteds"}),200