import requests
from helpers import generate_random_string, generate_random_email
import pytest
from data import Api


@pytest.fixture(scope="function")
def register_new_user():
    user_data = []
    name = generate_random_string(10)
    password = generate_random_string(10)
    email = generate_random_email(name)

    payload = {
        "name": name,
        "password": password,
        "email": email
    }
    response = requests.post(Api.USER_REGISTER, data=payload)

    if response.status_code == 200:
        r = response.json()
        access_token = r["accessToken"]
        refresh_token = r["refreshToken"]

        user_data.append(name)
        user_data.append(password)
        user_data.append(email)
        user_data.append(access_token)
        user_data.append(refresh_token)

    yield user_data

    # if response.status_code == 201 and user_id is not None:
    #     # Финализатор для удаления созданного курьера
    #     requests.delete(f"{Api.COURIER}/{user_id}")


@pytest.fixture(scope="function")
def generate_random_user_data():
    name = generate_random_string(10)
    password = generate_random_string(10)
    email = generate_random_email(name)
    return name, password, email
