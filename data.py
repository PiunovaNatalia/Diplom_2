import json


class StatusCode:
    OK_200 = 200
    CREATED_201 = 201
    UNAUTHORIZED_401 = 401
    NOT_FOUND_404 = 404
    FORBIDDEN_403 = 403
    BAD_REQUEST_400 = 400
    CONFLICT_409 = 409
    INTERNAL_SERVER_ERROR_500 = 500
    GATEWAY_TIMEOUT_504 = 504


class Api:
    # Главный URL
    url = "https://stellarburgers.nomoreparties.site"

    # Заказы
    ORDERS = f"{url}/api/orders"

    # Пользователь
    USER_REGISTER = f"{url}/api/auth/register"
    USER_LOGIN = f"{url}/api/auth/login"
    USER_LOGOUT = f"{url}/api/auth/logout"
    USER_INFO = f"{url}/api/auth/user"
    TOKEN_REFRESH = f"{url}/api/auth/token"


class ResponseMessage:
    CREATED_RESPONSE = {'ok': True}
    REQUIRED_FIELDS_NOT_FOUND = "Недостаточно данных для создания учетной записи"
    REQUIRED_FIELDS_NOT_FOUND_FOR_LOGIN = "Недостаточно данных для входа"
    LOGIN_EXISTS = "Этот логин уже используется. Попробуйте другой."
    USER_NOT_FOUND = "Учетная запись не найдена"

class Data:
    pass