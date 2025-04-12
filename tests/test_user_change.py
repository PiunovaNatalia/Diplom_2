import allure
import requests

from data import StatusCode, Api, ResponseMessage


class TestUserChange:
    @allure.title("Тестирование изменения пользователя с авторизацией")
    def test_user_change_with_auth(self, register_new_user):
        user_data = register_new_user
        new_email = f"new_{user_data['email']}"

        response = requests.patch(
            url=Api.AUTH_USER,
            headers={"authorization": user_data["access_token"]},
            data={
                "email": new_email,
            },
        )
        new_email_from_response = response.json()["user"]["email"]

        assert (
                response.status_code == StatusCode.OK_200
                and response.json()["success"] == True
                and new_email == new_email_from_response
        )

    @allure.title("Тестирование изменения пользователя без авторизации")
    def test_user_change_without_auth(self, register_new_user):
        user_data = register_new_user
        new_email = f"new_{user_data['email']}"

        response = requests.patch(
            url=Api.AUTH_USER,
            data={
                "email": new_email,
            },
        )

        assert (
            response.status_code == StatusCode.UNAUTHORIZED_401
            and response.json()["success"] == False
            and response.json()["message"] == ResponseMessage.UNAUTHORIZED
        )
