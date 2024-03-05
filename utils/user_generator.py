import string
import random

from model.user_model.user import User


def generate_user_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = f'{generate_random_string(5)}@{generate_random_string(5)}.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)

    return User(login, password, name)
