import allure
import requests

from client.order_client import OrderClient
from model.order_model.order import Order
from model.user_model.user_token import UserToken
from utils.user_generator import generate_user_data


class TestGetOrderList:
    @allure.title('Test to get order list by logged in user')
    @allure.description('Get order list by with user authorization positive check')
    def test_get_orders_with_authorization_token(self, get_ingredients, prepare_user):
        new_user = generate_user_data()
        (_, token) = prepare_user(new_user)

        new_order = Order(get_ingredients[0:3])
        OrderClient().create_order(new_order, token)

        (data, status_code) = OrderClient().get_order_list(token)

        assert status_code == requests.codes['ok']
        assert data['success'] == True
        assert data['total'] == 1

    @allure.title('Test to get order list by non logged in user')
    @allure.description('Get order list by without user authorization negative check')
    def test_get_orders_without_authorization_token(self, get_ingredients):
        new_order = Order(get_ingredients[0:3])
        OrderClient().create_order(new_order, UserToken('', ''))

        (data, status_code) = OrderClient().get_order_list(UserToken('', ''))
        assert status_code == requests.codes['unauthorized']
        assert data['success'] == False
        assert data['message'] == 'You should be authorised'
