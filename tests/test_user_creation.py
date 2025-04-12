import allure
import requests

from data import StatusCode, Api, ResponseMessage


class TestUserCreation:
    @allure.title("Тестирование создания уникального пользователя")
    def test_user_creation_unique_user(self, generate_random_user_data):
        user_data = generate_random_user_data
        payload = {
            "name": user_data["name"],
            "password": user_data["password"],
            "email": user_data["email"],
        }
        response = requests.post(Api.USER_REGISTER, data=payload)

        assert (
                response.status_code == StatusCode.OK_200
                and response.json()["success"] == True
        )

    @allure.title("Тестирование создания пользователя с данными существующего пользователя")
    def test_user_creation_if_already_exist(self, register_new_user):
        user_data = register_new_user
        payload = {
            "name": user_data["name"],
            "password": user_data["password"],
            "email": user_data["email"],
        }
        response = requests.post(Api.USER_REGISTER, data=payload)

        assert (
            response.status_code == StatusCode.FORBIDDEN_403
            and response.json()["success"] == False
            and response.json()["message"] == ResponseMessage.ALREADY_EXISTS
        )

    @allure.title("Тестирование создания пользователя без заполнения обязательных полей")
    def test_user_creation_no_required_field_provided(self, generate_random_user_data):
        user_data = generate_random_user_data

        payload = {
            "name": user_data["name"],
            "password": user_data["password"],
        }
        response = requests.post(Api.USER_REGISTER, data=payload)

        assert(
            response.status_code == StatusCode.FORBIDDEN_403
            and response.json()["success"] == False
            and response.json()["message"] == ResponseMessage.NO_REQUIRED_FIELD_PROVIDED
        )
