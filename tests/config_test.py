
from werkzeug.security import generate_password_hash
from src import create_app,db
from src.models import User
import pytest

api = create_app(':memory:')

@pytest.fixture()
def app():
    
    api = create_app(':memory:')
    
    with api.app_context():
        
        db.create_all()
        
        password = generate_password_hash("teste123")
        user = User(name="Jhon", phone="81997564326", email="teste@gmail.com", password=password)
        
        db.session.add(user)
        db.session.commit()

        yield api
        
        db.session.remove()
        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()
        