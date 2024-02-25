import requests
import allure

from client.user_client import UserClient
from model.user_model.user import User
from model.user_model.user_token import UserToken
from utils.user_generator import generate_user_data


class TestCreateUser:
    @allure.title('User creation test')
    @allure.description('User creation positive check')
    def test_create_user(self, delete_user):
        payload = generate_user_data()
        (data, status_code) = UserClient().create_user(payload)

        assert status_code == requests.codes['ok']
        assert data['success'] == True
        assert data['user']['email'] == payload.email
        assert data['user']['name'] == payload.name
        assert data['accessToken'] is not None
        assert data['refreshToken'] is not None

        delete_user(UserToken(data['accessToken'], data['refreshToken']))

    @allure.title('Double user creation test')
    @allure.description('Double user creation negative check')
    def test_create_double_user(self, delete_user):
        payload = generate_user_data()
        (first_user, _) = UserClient().create_user(payload)
        (data, status_code) = UserClient().create_user(payload)

        assert status_code == requests.codes['forbidden']
        assert data['success'] == False
        assert data['message'] == 'User already exists'

        delete_user(UserToken(first_user['accessToken'], first_user['refreshToken']))

    @allure.title('User creation without required fields test')
    @allure.description('User creation without email negative check')
    def test_create_user_without_email(self):
        payload = User('', 'beer123', 'Misato')
        (data, status_code) = UserClient().create_user(payload)

        assert status_code == requests.codes['forbidden']
        assert data['success'] == False
        assert data['message'] == 'Email, password and name are required fields'
