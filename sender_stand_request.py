import configuration
import requests
import data

def post_new_user(body): #ф-ия создания нового пользователя, в рез-те получаем токен в словаре
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def new_name_create_kit (kit_body): #боди для передачи в запрос создания набора с тестируемым name
    current_kit_body = data.new_kit_body.copy()
    current_kit_body["name"] = kit_body
    return current_kit_body

def new_token(): # хэдер с актуальным токеном
    response = post_new_user(data.user_body)
    dict = response.json()  # получить словарь из объекта Response
    auth_token = dict['authToken']  # переменная, которая хранит актуальный токен
    current_headers_create_kit = data.headers.copy()
    current_headers_create_kit["Authorization"] = "Bearer " + auth_token
    return current_headers_create_kit

def post_new_client_kit(kit_body): # ф-ия создания набора и получения тестируемого body в ответ
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=new_name_create_kit(kit_body),
                         headers=new_token())