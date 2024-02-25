import pytest

from client.user_client import UserClient
from model.user_model.user import User
from model.user_model.user_credentials import UserCredentials
from model.user_model.user_token import UserToken


@pytest.fixture(scope='function')
def prepare_user():
    user_client = UserClient()

    user = {}
    user_token = {}

    def _prepare_user(data: User):
        nonlocal user
        nonlocal user_token

        user_client.create_user(data)
        (login_response, _) = user_client.login_user(UserCredentials(data.email, data.password))

        user = data
        user_token = UserToken(login_response['accessToken'], login_response['refreshToken'])

        return user, user_token

    yield _prepare_user

    user_client.delete_user(user_token)


@pytest.fixture(scope='function')
def delete_user():
    user_client = UserClient()
    token = {}

    def _delete_user(data: UserToken):
        nonlocal token
        token = data

    yield _delete_user

    user_client.delete_user(token)
