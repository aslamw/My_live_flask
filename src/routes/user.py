from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..controllers import ControllerUser
import json

api_user = Blueprint("user", __name__)


@api_user.get("/")
def home():
    return jsonify({"mensage": "ok"}), 200


@api_user.post("/register")
def register():
    data: dict = json.loads(request.data)
    return ControllerUser.register_user(data)


@api_user.post("/login")
def user_login():
    data = json.loads(request.data)

    return ControllerUser.login(data)


@api_user.get("/user")
@jwt_required()
def user():
    id = get_jwt_identity()
    return ControllerUser.get_data_user(id)


@api_user.put("/user/update")
@jwt_required()
def update_user():
    id = get_jwt_identity()

    data = json.loads(request.data)

    return ControllerUser.update_user(id, data)


@api_user.delete("/user/delete")
@jwt_required()
def delete_user():
    id = get_jwt_identity()

    return ControllerUser.delete_user(id)
