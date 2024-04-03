from .config_test import client, app
from src.models import User,Daily
import  json


# The `TestUser` class contains methods for testing user registration, login, retrieval, update, and
# deletion functionality in a Flask application.
class TestUser:
    
    def token_user(self,client):#Utilitário 
        """
        The function `token_user` is a utility function that takes a `client` object and returns the
        token obtained from a login request made with the given client.
        
        :param client: The `client` parameter is an object that represents the HTTP client used to make
        requests to the server. It is typically an instance of a library like `requests` or
        `http.client`. In this case, it is used to make a POST request to the `/login` endpoint
        :return: the token value extracted from the response of a POST request to the '/login' endpoint.
        """
        
        login_valid = client.post('/login', data=json.dumps({"email":"teste@gmail.com", "password":"teste123"}))
        
        return dict(json.loads(login_valid.data.decode('utf-8')))['token']
    
    def test_func(self,client):
        """
        The function `test_func` sends a GET request to the root URL ("/") using the `client` object and
        asserts that the response status code is 200.
        
        :param client: The "client" parameter is an instance of a test client that is used to simulate
        HTTP requests in unit tests. It allows you to make requests to your application and assert the
        responses. In this case, the "get" method is used to send a GET request to the root URL ("/") of
        """
        """
        The function tests if the response status code from a client's GET request to '/' is equal to
        200.
        
        :param client: The "client" parameter is an instance of a test client that is used to simulate
        HTTP requests in unit tests. It allows you to make requests to your application and assert the
        responses. In this case, the "get" method is used to send a GET request to the root URL ("/") of
        """
        
        response = client.get('/')
        
        assert response.status_code == 200
        

    def test_register(self,client):
        """
        The function `test_register` tests the registration functionality by sending a POST request with
        user data and asserting that the response status code is 201, the number of users in the database
        is 2, and the user with the specified email exists in the database.
        
        :param client: The "client" parameter is an instance of a client object that is used to make HTTP
        requests to the server. It is typically used in testing frameworks to simulate requests and test
        the server's response. In this case, it is used to make a POST request to the '/register' endpoint
        with the
        """
        data_user = {"name":"jan","phone":"81993567865","email":"teste_J@gmail.com", "password":"teste123"}
        
        response = client.post('/register',data=json.dumps(data_user))
        
        
        assert response.status_code == 201
        assert User.query.count() == 2
        assert User.query.filter(User.email == "teste_J@gmail.com").count() == 1
    

    def test_login(self,client):
        """
        The function `test_login` tests the login functionality by making POST requests with valid and
        invalid credentials and asserting the expected status codes.
        
        :param client: The `client` parameter is an instance of a test client that is used to make HTTP
        requests to your application. It allows you to simulate requests and test the behavior of your
        application without actually running it in a server
        """
     
        login_valid = client.post('/login', data=json.dumps({"email":"teste@gmail.com", "password":"teste123"}))
        
        login_invalid = client.post('/login', data=json.dumps({"email":"teste@gmail.com", "password":"teste1234"}))
        
        assert login_valid.status_code == 200
        assert login_invalid.status_code == 401
        
    def test_get_user(self,client):
        """
        The function `test_get_user` tests the functionality of the `get_user` endpoint by making a GET
        request with a valid token and asserting that the response contains the expected user email and
        has a status code of 200.
        
        :param client: The `client` parameter is an instance of the Flask test client. It is used to
        simulate HTTP requests to your Flask application during testing
        """
        
        token = self.token_user(client)
        
        
        response = client.get('/user',headers = {'Authorization': f'Bearer {token}'})
        
        assert dict(json.loads(response.data.decode('utf-8')))['user']['email'] == "teste@gmail.com"
        assert response.status_code == 200
        
    def test_update_user(self,client):
        """
        The function `test_update_user` tests the functionality of updating a user's name using a PUT
        request.
        
        :param client: The `client` parameter is an instance of the Flask test client. It is used to
        simulate HTTP requests to your Flask application during testing
        """
        
        token = self.token_user(client)  
        response = client.put('/user/update', data = json.dumps({"name":"Yan"}), headers = {'Authorization': f'Bearer {token}'})
        
        assert User.query.filter(User.name == "Yan").count() == 1
        assert response.status_code == 200
        
    def test_delete_user(self,client):
        """
        The function `test_delete_user` tests the functionality of deleting a user by sending a DELETE
        request to the `/user/delete` endpoint with the user's token in the Authorization header, and
        asserts that the user is deleted from the database and the response status code is 200.
        
        :param client: The `client` parameter is an instance of the Flask test client. It is used to
        simulate HTTP requests to your Flask application during testing
        """
        
        token = self.token_user(client)
        
        
        response = client.delete('/user/delete', headers = {'Authorization': f'Bearer {token}'})
        
        assert User.query.filter(User.email == "teste@gmail.com").count() == 0
        assert response.status_code == 200



# The `TestDaily` class contains test methods for testing the functionality of adding, retrieving,
# updating, and deleting annotations using a Flask test client.
class TestDaily(TestUser):
    
    def test_add_annotation(self,client):
        """
        The function `test_add_annotation` tests the functionality of adding an annotation to a daily
        entry using a client object.
        
        :param client: The `client` parameter is an instance of the Flask test client. It is used to
        simulate HTTP requests to your Flask application during testing
        """
        
        token = self.token_user(client)
        
        response = client.post('/annotation', data = json.dumps({"text":"oi"}), headers = {'Authorization': f'Bearer {token}'})
        
        assert response.status_code == 200
        assert Daily.query.filter(Daily.annotation == "oi").count() == 1
        assert dict(json.loads(response.data.decode('utf-8')))['annotation'] == 'oi'
        
    def test_get_all_annotation(self,client):
        """
        The function `test_get_all_annotation` sends a GET request to the '/annotation/all' endpoint
        with an authorization token and asserts that the response status code is 200.
        
        :param client: The `client` parameter is an instance of the Flask test client. It is used to
        simulate HTTP requests to your Flask application during testing
        """
        
        token = self.token_user(client)
        
        response = client.get('/annotation/all', headers = {'Authorization': f'Bearer {token}'})
        
        assert response.status_code == 200
        
        
    def test_get_annotation(self,client):
        """
        The function `test_get_annotation` tests the functionality of retrieving an annotation by its ID
        using the `GET` method.
        
        :param client: The `client` parameter is an instance of a HTTP client that is used to make
        requests to the server. It is typically used in testing frameworks to simulate HTTP requests and
        receive responses from the server
        """
        
        token = self.token_user(client)
        
        client.post('/annotation', data = json.dumps({"text":"oi"}), headers = {'Authorization': f'Bearer {token}'})
        
        response = client.get('/annotation/1', headers = {'Authorization': f'Bearer {token}'})
        
        assert response.status_code == 200
        
        
    def test_update_annotation(self,client):
        """
        The function `test_update_annotation` tests the functionality of updating an annotation by
        sending a POST request to create an annotation and then a PUT request to update it.
        
        :param client: The "client" parameter is an instance of the Flask test client. It is used to
        make HTTP requests to the application being tested
        """
        
        token = self.token_user(client)
        client.post('/annotation', data = json.dumps({"text":"oi"}), headers = {'Authorization': f'Bearer {token}'})
        
        response = client.put('/annotation/update/1', data = json.dumps({"text":"bom dia"}), headers = {'Authorization': f'Bearer {token}'})
        
        assert response.status_code == 200
        
        
    def test_delete_annotation(self,client):
        """
        The function `test_delete_annotation` tests the deletion of an annotation by making a POST
        request to create an annotation and then a DELETE request to delete it, and asserts that the
        response status code is 200 and that the annotation is no longer present in the database.
        
        :param client: The `client` parameter is an instance of a Flask test client. It is used to make
        HTTP requests to the Flask application being tested
        """
        
        token = self.token_user(client)
        client.post('/annotation', data = json.dumps({"text":"oi"}), headers = {'Authorization': f'Bearer {token}'})
        
        response = client.delete('/annotation/delete/1', headers = {'Authorization': f'Bearer {token}'})
        
        assert response.status_code == 200
        assert Daily.query.filter(Daily.id == 1).count() == 0
    