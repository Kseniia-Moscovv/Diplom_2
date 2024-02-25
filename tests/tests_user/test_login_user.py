import requests
import allure

from client.user_client import UserClient
from model.user_model.user_credentials import UserCredentials
from utils.user_generator import generate_user_data


class TestCreateUser:
    @allure.title('User login test')
    @allure.description('User login positive check')
    def test_create_user(self, prepare_user):
        payload = generate_user_data()
        (user, _) = prepare_user(payload)

        (data, status_code) = UserClient().login_user(UserCredentials(user.email, user.password))

        assert status_code == requests.codes['ok']
        assert data['success'] == True
        assert data['user']['email'] == user.email
        assert data['user']['name'] == user.name
        assert data['accessToken'] is not None
        assert data['refreshToken'] is not None

    @allure.title('User login without required fields test')
    @allure.description('User login with incorrect login and password negative check')
    def test_login_user_without_pass(self, prepare_user):
        payload = generate_user_data()
        (user, _) = prepare_user(payload)

        (data, status_code) = UserClient().login_user(UserCredentials('misato_katsuragi@evangelion.jp', 'beer123'))

        assert status_code == requests.codes['unauthorized']
        assert data['success'] == False
        assert data['message'] == 'email or password are incorrect'

