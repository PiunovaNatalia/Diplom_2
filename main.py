import random
import string, requests
from data import Api


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_random_email(login):
    return f"{login}_{generate_random_string(5)}@testmail.ru"


login_pass = []
user_id = None

name = generate_random_string(10)
password = generate_random_string(10)
email = generate_random_email(name)

payload = {
    "name": name,
    "password": password,
    "email": email
}

response = requests.post(Api.USER_REGISTER, data=payload)
r = response.json()
access_token = r["accessToken"]
refresh_token = r["refreshToken"]

# response = requests.post(Api.USER_LOGIN, data=payload)
# print(response.json())

payload = {
    "authorization": f"{access_token}"
}
response = requests.delete(Api.USER_INFO, headers=payload)

# {'success': True, 'message': 'User successfully removed'}
# 202


print(response.json())
#
#
# d = {
#     "success": True,
#     "user":{
#         "email":"wnmeugtqaa_zlkkd@testmail.ru",
#         "name":"wnmeugtqaa"
#     },
#      "accessToken":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3ZjRjM2M3OWVkMjgwMDAxYjViYWY4ZSIsImlhdCI6MTc0NDA5NDE1MSwiZXhwIjoxNzQ0MDk1MzUxfQ.skmYNLOToO__NwhASD6xLRCYFirmvRrAcTb4iNfGGXY",
#      "refreshToken":"7d6597e537b40eff33b52a31fd40d028a103b555957c0b465054563ee7968ee867bf7bfbabeaec31"
# }
# import json

print(response.status_code)
