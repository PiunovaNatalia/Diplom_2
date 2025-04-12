import allure
import requests
import pytest

from data import StatusCode, Api, Data, ResponseMessage


class TestOrderCreation:
    @pytest.mark.parametrize('order_data', Data.ORDERS_DATA)
    @allure.title("Тестирование создания заказа с авторизацией и ингредиентами")
    def test_order_creation_with_auth_and_with_ingredients(self, order_data, register_new_user):
        user_data = register_new_user

        ingredients = order_data["ingredients"]
        expected_result = order_data["expected_result"]

        response = requests.post(
            url=Api.ORDERS,
            headers={"authorization": user_data["access_token"]},
            data={"ingredients": ingredients},
        )
        order = response.json()

        assert (
                response.status_code == StatusCode.OK_200
                and order["success"] == True
                and order["name"] == expected_result
        )

    @allure.title("Тестирование создания заказа с авторизацией и БЕЗ ингредиентов")
    def test_order_creation_with_auth_and_without_ingredients(self, register_new_user):
        user_data = register_new_user

        response = requests.post(
            url=Api.ORDERS,
            headers={"authorization": user_data["access_token"]},
        )

        assert (
                response.status_code == StatusCode.BAD_REQUEST_400
                and response.json()["success"] == False
                and response.json()["message"] == ResponseMessage.INGREDIENTS_REQUIRED
        )

    @pytest.mark.parametrize('order_data', Data.ORDERS_DATA)
    @allure.title("Тестирование создания заказа без авторизации и с ингредиентами")
    def test_order_creation_without_auth_and_with_ingredients(self, order_data, register_new_user):
        user_data = register_new_user
        ingredients = order_data["ingredients"]
        expected_result = order_data["expected_result"]
        response = requests.post(
            url=Api.ORDERS,
            data={"ingredients": ingredients},
        )
        order = response.json()

        assert (
                response.status_code == StatusCode.OK_200
                and order["success"] == True
                and order["name"] == expected_result
        )

    @allure.title("Тестирование создания заказа БЕЗ авторизации и БЕЗ ингредиентов")
    def test_order_creation_without_auth_and_without_ingredients(self, register_new_user):
        user_data = register_new_user
        response = requests.post(url=Api.ORDERS)

        assert (
                response.status_code == StatusCode.BAD_REQUEST_400
                and response.json()["success"] == False
                and response.json()["message"] == ResponseMessage.INGREDIENTS_REQUIRED
        )

    @pytest.mark.parametrize('ingredients', Data.ORDERS_WRONG_INGREDIENT_DATA)
    @allure.title("Тестирование создания заказа с авторизацией и неверными хешами ингредиентов")
    def test_order_creation_with_auth_and_wrong_ingredients_hashes(self, ingredients, register_new_user):
        user_data = register_new_user
        response = requests.post(
            url=Api.ORDERS,
            headers={"authorization": user_data["access_token"]},
            data={"ingredients": ingredients},
        )

        assert response.status_code == StatusCode.INTERNAL_SERVER_ERROR_500
