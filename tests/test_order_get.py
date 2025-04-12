import allure
import requests
import pytest

from data import StatusCode, Api, Data, ResponseMessage


class TestOrderCreation:
    @pytest.mark.parametrize('order_data', Data.ORDERS_DATA)
    @allure.title("Тестирование получения заказов авторизованного пользователя")
    def test_order_get_order_with_auth(self, order_data, register_new_user):
        user_data = register_new_user
        ingredients = order_data["ingredients"]
        requests.post(
            url=Api.ORDERS,
            headers={"authorization": user_data["access_token"]},
            data={"ingredients": ingredients},
        )
        response = requests.get(
            url=Api.ORDERS,
            headers={"authorization": user_data["access_token"]},
        )

        assert (
                response.status_code == StatusCode.OK_200
                and response.json()["success"] == True
                and len(response.json()["orders"]) == 1
        )

    @pytest.mark.parametrize('order_data', Data.ORDERS_DATA)
    @allure.title("Тестирование получения заказов авторизованного пользователя")
    def test_order_get_order_with_auth(self, order_data, register_new_user):
        user_data = register_new_user
        requests.post(
            url=Api.ORDERS,
            headers={"authorization": user_data["access_token"]},
            data={"ingredients": order_data["ingredients"]},
        )
        response = requests.get(url=Api.ORDERS)

        assert (
                response.status_code == StatusCode.UNAUTHORIZED_401
                and response.json()["success"] == False
                and response.json()["message"] == ResponseMessage.UNAUTHORIZED
        )
