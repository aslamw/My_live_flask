from flask import request, jsonify
from functools import wraps
from ..models import create_user, get_user
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
import json, re, os

#fomat valid email
F_email = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')

def register_user():
    data = json.loads(request.data)
    
    if not data['name'] or not data['phone'] or not data['password'] or not data['email']:
        return jsonify({"menssage":"All fields are mandatory"}),400
    
    if not data["name"].isalpha():
        return jsonify({"menssage":"name invalid"}),400
    
    if not F_email.match(data['email']):
        return jsonify({"menssage":"E-mail invalid"}),400
    
    data["password"] = generate_password_hash(data['password'])
    
    state = create_user(data)
    """ if state:
        return jsonify({"menssage":"success create"}),201
    else: jsonify({"menssage":"error"}),400 """
    
    return jsonify({"menssage":"success create"},state),201
    
def logi(id):
    pass
        