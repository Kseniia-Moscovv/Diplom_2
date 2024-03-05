import allure
import requests

from client.order_client import OrderClient
from model.order_model.order import Order
from model.user_model.user_token import UserToken
from utils.user_generator import generate_user_data


class TestCreateOrder:
    @allure.title('Order creation test by logged in user')
    @allure.description('Order creation with user authorization positive check')
    def test_create_order_with_authorization_token(self, get_ingredients, prepare_user):
        new_user = generate_user_data()
        (_, token) = prepare_user(new_user)

        payload = Order(get_ingredients[0:3])
        (data, status_code) = OrderClient().create_order(payload, token)

        assert status_code == requests.codes['ok']
        assert data['success'] == True
        assert data['name'] is not None
        assert data['order']['number'] is not None

    @allure.title('Order creation test by non logged in user')
    @allure.description('Order creation without user authorization negative check')
    def test_create_order_without_authorization_token(self, get_ingredients):
        payload = Order(get_ingredients[0:3])
        (data, status_code) = OrderClient().create_order(payload, UserToken('', ''))

        assert status_code == requests.codes['unauthorized']
        assert data['success'] == False

    @allure.title('Order creation test without ingredients')
    @allure.description('Order creation without request body negative check')
    def test_create_order_with_authorization_token(self, prepare_user):
        new_user = generate_user_data()
        (_, token) = prepare_user(new_user)

        (data, status_code) = OrderClient().create_order(Order([]), token)

        assert status_code == requests.codes['bad_request']
        assert data['success'] == False
        assert data['message'] == 'Ingredient ids must be provided'

    @allure.title('Order creation test with non existent ingredients')
    @allure.description('Order creation with incorrect request body negative check')
    def test_create_order_with_authorization_token(self, prepare_user):
        new_user = generate_user_data()
        (_, token) = prepare_user(new_user)

        (data, status_code) = OrderClient().create_order(Order(['donut', 'cream', 'jam']), token)

        assert status_code == requests.codes['internal_server_error']
