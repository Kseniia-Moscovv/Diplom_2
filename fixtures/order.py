import pytest

from client.order_client import OrderClient


@pytest.fixture(scope='function')
def get_ingredients():
    (result, _) = OrderClient().get_ingredients_list()
    data = result['data']

    ingredients = []
    for ingredient in data:
        ingredients.append(ingredient['_id'])

    return ingredients




