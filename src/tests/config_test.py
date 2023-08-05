
from werkzeug.security import generate_password_hash
from .. import create_app
from ..models import User
import pytest

api,_db = create_app()

@pytest.fixture(scope='module')
def app():
    app = api
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        
        _db.create_all()
        
        password = generate_password_hash("teste123")
        user = User(name="Jhon", phone="81997564321", email="teste@gmail.com", password=password)
        
        _db.session.add(user)
        _db.session.commit()
        
        

        yield app

        _db.session.remove()
        _db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    with app.test_client() as client:
        yield client
        
        
""" @pytest.fixture
def db(app):
    
    with app.app_context():
        
        _db.create_all()
        
        password = generate_password_hash("teste123")
        user = User(name="Jhon", phone="81997564321", email="teste@gmail.com", password=password)
        
        _db.session.add(user)
        _db.session.commit()
        
        yield db
        
        _db.drop_all()
        
        """
        