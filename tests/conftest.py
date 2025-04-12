import requests
from helpers import generate_random_string, generate_random_email
import pytest
from data import Api


@pytest.fixture(scope="function")
def register_new_user():

    name = generate_random_string(10)
    password = generate_random_string(10)
    email = generate_random_email(name)

    payload = {
        "name": name,
        "password": password,
        "email": email
    }
    response = requests.post(Api.USER_REGISTER, data=payload)

    user_data = {
        "name": name,
        "email": email,
        "password": password,
        "access_token": response.json()["accessToken"],
        "refresh_token": response.json()["refreshToken"],
    }

    yield user_data

    # Удаляем пользователя
    requests.delete(Api.AUTH_USER, headers={"authorization": response.json()["accessToken"]})


@pytest.fixture(scope="function")
def generate_random_user_data():
    name = generate_random_string(10)
    password = generate_random_string(10)
    email = generate_random_email(name)

    return {
        "name": name,
        "password": password,
        "email": email,
    }
