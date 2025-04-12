import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_random_email(login):
    return f"{login}_{generate_random_string(5)}@testmail.ru"
