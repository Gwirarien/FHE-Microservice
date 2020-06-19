import pytest
import app

import warnings
warnings.simplefilter("ignore", category=PendingDeprecationWarning)

def test_login_route():
    test_app = app.create_app()
    with test_app.test_client() as client:
        response = client.get('/login')
        assert response.status_code == 200

def test_register_route():
    test_app = app.create_app()
    with test_app.test_client() as client:
        response = client.get('/register')
        assert response.status_code == 200
        
def test_unauthorized_post_route():
    test_app = app.create_app()
    with test_app.test_client() as client:
        response = client.get('/post/1')
        assert response.status_code == 403

def test_unknown_route():
    test_app = app.create_app()
    with test_app.test_client() as client:
        response = client.get('/test_route')
        assert response.status_code == 404

def test_calculate_route():
    test_app = app.create_app()
    with test_app.test_client() as client:
        response = client.get('/calculate')
        assert response.status_code == 200
    
def test_home_route():
    test_app = app.create_app()
    with test_app.test_client() as client:
        response_index = client.get('/')
        response_home = client.get('/home')
        assert response_index.status_code == 200
        assert response_home.status_code == 200

def test_about_privacy_route():
    test_app = app.create_app()
    with test_app.test_client() as client:
        response = client.get('/about_privacy')
        assert response.status_code == 200

