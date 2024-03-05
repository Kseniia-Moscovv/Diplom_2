import allure
import requests

from client.user_client import UserClient
from constants.user_data_constants import UpdateUserData
from model.user_model.user import User
from model.user_model.user_token import UserToken
from utils.user_generator import generate_user_data


class TestUpdateUser:
    @allure.title('User update without authorization test')
    @allure.description('User update login, pass, name fields positive check')
    def test_update_user(self, prepare_user):
        payload = generate_user_data()
        (user, token) = prepare_user(payload)
        (data, status_code) = UserClient().update_user(
            User(UpdateUserData.NEW_EMAIL, UpdateUserData.NEW_PASSWORD, UpdateUserData.NEW_NAME),
            token
        )

        assert status_code == requests.codes['ok']
        assert data['success'] == True
        assert data['user']['email'] == UpdateUserData.NEW_EMAIL
        assert data['user']['name'] == UpdateUserData.NEW_NAME

    @allure.title('User update without authorization test')
    @allure.description('User update login, pass, name fields without authorization negative check')
    def test_update_user(self, prepare_user):
        payload = generate_user_data()
        (user, _) = prepare_user(payload)
        (data, status_code) = UserClient().update_user(
            User(UpdateUserData.NEW_EMAIL, UpdateUserData.NEW_PASSWORD, UpdateUserData.NEW_NAME),
            UserToken('', '')
        )

        assert status_code == requests.codes['unauthorized']
        assert data['success'] == False
        assert data['message'] == 'You should be authorised'
