from .config_test import client, app
import pytest

@pytest.mark.usefixtures('app')
class TestUser:
    
    @pytest.mark.usefixtures('client')
    def test_login(self, client):
        
        response = client.post('/login',data={"email":"teste@gmail.com", "password":"teste123"})
        
        assert response.status_code == 200