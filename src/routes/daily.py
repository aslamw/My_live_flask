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

@api_daily.get('/all')
@jwt_required()
def get_all():
    id = get_jwt_identity()
    return ControllersDaily.get_all(id)

@api_daily.get('/annotation/<int:id>')
@jwt_required()
def get(id):
    id_user = get_jwt_identity()
    return ControllersDaily.get_annotation(id,id_user)

@api_daily.put('/anotation/update')
@jwt_required()
def update_user():
    id = get_jwt_identity()
    
    data = json.loads(request.data)
    
    return 'ok'


@api_daily.delete('/annotation/delete')
@jwt_required()
def delete_user():
    id = get_jwt_identity()
    
    return 'ok'