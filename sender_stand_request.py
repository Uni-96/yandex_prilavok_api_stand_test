import configuration
import requests
import data

def post_new_user(body): #ф-ия создания нового пользователя, в рез-те получаем токен в словаре
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(kit_body): # ф-ия создания набора
    response = post_new_user(data.user_body)
    dict = response.json()  # получить словарь из объекта Response
    key = 'authToken'
    auth_token = dict[key] #переменная, которая хранит актуальный токен
    current_kit_body = data.new_kit_body.copy()
    current_kit_body["name"] = kit_body
    current_headers_create_kit = data.headers_create_kit.copy()
    current_headers_create_kit["Authorization"] = "Bearer " + auth_token #хэдер с актуальным токеном
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=current_kit_body,
                         headers=current_headers_create_kit)

response = post_new_client_kit("Тестовый набор")
print(response.json())