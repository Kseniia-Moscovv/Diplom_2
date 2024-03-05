from client.base_client import BaseClient
from constants.url_constants import UrlConstants
from model.user_model.user import User
from model.user_model.user_credentials import UserCredentials
from model.user_model.user_token import UserToken


class UserClient(BaseClient):
    def create_user(self, user: User):
        return self.post(f'{UrlConstants.USER_URL}/register', user.__dict__)

    def login_user(self, user_credentials: UserCredentials):
        return self.post(f'{UrlConstants.USER_URL}/login', user_credentials.__dict__)

    def update_user(self, user_update: User, token: UserToken):
        return self.patch(f'{UrlConstants.USER_URL}/user', user_update.__dict__, token.to_dict())

    def delete_user(self, token: UserToken):
        return self.delete(url=f'{UrlConstants.USER_URL}/user', headers=token.to_dict())

