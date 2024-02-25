from client.base_client import BaseClient
from constants.url_constants import UrlConstants
from model.order_model.order import Order
from model.user_model.user_token import UserToken


class OrderClient(BaseClient):
    def get_ingredients_list(self):
        return self.get(f'{UrlConstants.BASE_URL}/ingredients')

    def create_order(self, order: Order, token: UserToken):
        return self.post(f'{UrlConstants.ORDER_URL}', order.__dict__, token.to_dict())

    def get_order_list(self, token: UserToken):
        return self.get(url=f'{UrlConstants.ORDER_URL}', headers=token.to_dict())
