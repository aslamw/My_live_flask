from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..controllers import ControllersDaily
import json

api_daily = Blueprint('daily', __name__)

@api_daily.post('/annotation')
@jwt_required()
def register():
    id = get_jwt_identity()
    data:dict = json.loads(request.data) 
    return ControllersDaily.register(id,data["text"])

@api_daily.get('/annotation/all')
@jwt_required()
def get_all():
    id = get_jwt_identity()
    return ControllersDaily.get_all(id)

@api_daily.get('/annotation/<int:id>')
@jwt_required()
def get(id):
    id_user = get_jwt_identity()
    return ControllersDaily.get_annotation(id,id_user)

@api_daily.put('/annotation/update/<int:id>')
@jwt_required()
def update_user(id):
    id_user = get_jwt_identity()
    
    data = json.loads(request.data)
    
    return ControllersDaily.update(id_user, id, data['text'])


@api_daily.delete('/annotation/delete/<int:id>')
@jwt_required()
def delete_user(id):
    id_user = get_jwt_identity()
    
    return ControllersDaily.delete(id, id_user)