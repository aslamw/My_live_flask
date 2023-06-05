from flask import Blueprint, request, jsonify
from ..controllers import register_user

api_user = Blueprint('user', __name__)

@api_user.get('/')
def home():
    return jsonify({"mensage":"ok"}), 200

@api_user.post('/register')
def register():
    return register_user()