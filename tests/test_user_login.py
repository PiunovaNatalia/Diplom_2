import allure
import requests

from data import StatusCode, Api, ResponseMessage


class TestUserLogin:
    @allure.title("Тестирование успешной авторизации пользователя")
    def test_user_successful_login(self, register_new_user):
        user_data = register_new_user
        payload = {
            "email": user_data["email"],
            "password": user_data["password"],
        }
        response = requests.post(Api.USER_LOGIN, data=payload)

        assert (
                response.status_code == StatusCode.OK_200
                and response.json()["success"] == True
        )

    @allure.title("Тестирование авторизации пользователя с неверным паролем")
    def test_user_wrong_password_login(self, register_new_user):
        user_data = register_new_user
        payload = {
            "email": user_data["email"],
            "password": user_data["password"] + "WRONG!",
        }
        response = requests.post(Api.USER_LOGIN, data=payload)

        assert (
            response.status_code == StatusCode.UNAUTHORIZED_401
            and response.json()["success"] == False
            and response.json()["message"] == ResponseMessage.INCORRECT_DATA
        )

    @allure.title("Тестирование авторизации пользователя с неверным имейлом")
    def test_user_wrong_email_login(self, register_new_user):
        user_data = register_new_user
        payload = {
            "email": user_data["email"] + "WRONG!",
            "password": user_data["password"],
        }
        response = requests.post(Api.USER_LOGIN, data=payload)

        assert (
            response.status_code == StatusCode.UNAUTHORIZED_401
            and response.json()["success"] == False
            and response.json()["message"] == ResponseMessage.INCORRECT_DATA
        )
