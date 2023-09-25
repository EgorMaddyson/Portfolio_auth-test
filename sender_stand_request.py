import configuration
import requests
import data

# Функция создания нового пользователя:
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.user_headers)

# print(post_new_user(data.user_body).json()["authToken"])  # = 5c71f64f-4f7c-4538-ab55-7436a9223c06

# Функция создания нового продуктового набора:
def post_new_client_kit(kit_body, auth_token):
    user_token = data.kit_headers.copy()
    user_token["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=user_token)