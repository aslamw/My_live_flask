from .config_test import client, app
from src.models import User,Daily
import pytest, json


class TestUser:
    
    def token_user(self,client):#Utilitário 
        
        login_valid = client.post('/login', data=json.dumps({"email":"teste@gmail.com", "password":"teste123"}))
        
        return dict(json.loads(login_valid.data.decode('utf-8')))['token']
    
    def test_func(self,client):
        
        response = client.get('/')
        
        assert response.status_code == 200
        

    def test_register(self,client):
        data_user = {"name":"jan","phone":"81993567865","email":"teste_J@gmail.com", "password":"teste123"}
        
        response = client.post('/register',data=json.dumps(data_user))
        
        
        assert response.status_code == 201
        assert User.query.count() == 2
        assert User.query.filter(User.email == "teste_J@gmail.com").count() == 1
    

    def test_login(self,client):
     
        login_valid = client.post('/login', data=json.dumps({"email":"teste@gmail.com", "password":"teste123"}))
        
        login_invalid = client.post('/login', data=json.dumps({"email":"teste@gmail.com", "password":"teste1234"}))
        
        assert login_valid.status_code == 200
        assert login_invalid.status_code == 401
        
    def test_get_user(self,client):
        
        #login_valid = client.post('/login', data=json.dumps({"email":"teste@gmail.com", "password":"teste123"}))
        
        token = self.token_user(client)
        
        
        response = client.get('/user',headers = {'Authorization': f'Bearer {token}'})
        
        assert dict(json.loads(response.data.decode('utf-8')))['user']['email'] == "teste@gmail.com"
        assert response.status_code == 200
        
    def test_update_user(self,client):
        
        token = self.token_user(client)
        
        
        response = client.put('/user/update', data = json.dumps({"name":"Yan"}), headers = {'Authorization': f'Bearer {token}'})
        
        assert User.query.filter(User.name == "Yan").count() == 1
        assert response.status_code == 200
        
    def test_delete_user(self,client):
        
        token = self.token_user(client)
        
        
        response = client.delete('/user/delete', headers = {'Authorization': f'Bearer {token}'})
        
        assert User.query.filter(User.email == "teste@gmail.com").count() == 0
        assert response.status_code == 200



class TestDaily(TestUser):
    
    def test_add_annotation(self,client):
        
        token = self.token_user(client)
        
        response = client.post('/annotation', data = json.dumps({"text":"oi"}), headers = {'Authorization': f'Bearer {token}'})
        
        assert response.status_code == 200
        assert Daily.query.filter(Daily.annotation == "oi").count() == 1
        assert dict(json.loads(response.data.decode('utf-8')))['annotation'] == 'oi'
        
    def test_get_all_annotation(self,client):
        
        token = self.token_user(client)
        
        response = client.get('/annotation/all', headers = {'Authorization': f'Bearer {token}'})
        
        assert response.status_code == 200
        
        
    def test_get_annotation(self,client):
        
        token = self.token_user(client)
        
        client.post('/annotation', data = json.dumps({"text":"oi"}), headers = {'Authorization': f'Bearer {token}'})
        
        response = client.get('/annotation/1', headers = {'Authorization': f'Bearer {token}'})
        
        assert response.status_code == 200
        
        
    def test_update_annotation(self,client):
        
        token = self.token_user(client)
        client.post('/annotation', data = json.dumps({"text":"oi"}), headers = {'Authorization': f'Bearer {token}'})
        
        response = client.put('/annotation/update/1', data = json.dumps({"text":"bom dia"}), headers = {'Authorization': f'Bearer {token}'})
        
        assert response.status_code == 200
        
        
    def test_delete_annotation(self,client):
        
        token = self.token_user(client)
        client.post('/annotation', data = json.dumps({"text":"oi"}), headers = {'Authorization': f'Bearer {token}'})
        
        response = client.delete('/annotation/delete/1', headers = {'Authorization': f'Bearer {token}'})
        
        assert response.status_code == 200
        assert Daily.query.filter(Daily.id == 1).count() == 0
    