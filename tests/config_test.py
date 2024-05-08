
from werkzeug.security import generate_password_hash
from src import create_app,db
from src.models import User
import pytest



@pytest.fixture()
def app():
    """
    The `app` function creates a Flask application, initializes the database, adds a user to the
    database, and then yields the application.
    """
    
    app = create_app('testing')
    
    with app.app_context():
        
        db.create_all()
        
        password = generate_password_hash("teste123")
        user = User(name="Jhon", phone="81997564326", email="teste@gmail.com", password=password)
        
        db.session.add(user)
        db.session.commit()

        yield app
        
        db.session.remove()
        db.drop_all()

@pytest.fixture()
def client(app):
    """
    The function `client` returns a test client for the given Flask application.
    
    :param app: The "app" parameter is an instance of a Flask application. It is used to create a test
    client for the application. The test client allows you to send HTTP requests to the application and
    receive the responses for testing purposes
    :return: an instance of the test client for the given Flask application.
    """
    return app.test_client()
        