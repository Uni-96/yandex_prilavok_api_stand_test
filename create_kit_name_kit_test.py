import configuration
import sender_stand_request
import requests
import data

# Функция для позитивной проверки
def positive_assert(kit_body):
    kit_body_response = sender_stand_request.post_new_client_kit(kit_body)
    # Проверяется, что код ответа равен 201
    assert kit_body_response.status_code == 201
    assert kit_body_response.json()["name"] == kit_body

# Функция для негативной проверки
def negative_assert(kit_body):
    kit_body_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_body_response.status_code == 400

# Тест 1: Допустимое количество символов (1)
def test_create_kit_1_letter_name_get_success_response():
    positive_assert("a")

# Тест 2: Допустимое количество символов (511)
def test_create_kit_511_letter_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3: Допустимое количество символов (0)
def test_create_kit_0_letter_name_get_success_response():
    positive_assert("")

# Тест 4: Неопустимое количество символов (512)
def test_create_kit_512_letter_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5: Разрешены английские буквы:
def test_create_kit_eng_letter_name_get_success_response():
    positive_assert("QWErty")

# Тест 6: Разрешены русские буквы:
def test_create_kit_rus_letter_name_get_success_response():
    positive_assert("Мария")

# Тест 7: Разрешены спецсимволы:
def test_create_kit_simbol_name_get_success_response():
    positive_assert("\"№%@\",")

# Тест 8: Разрешены пробелы
def test_create_kit_space_name_get_success_response():
    positive_assert("Человек и КО")

# Тест 9: Разрешены цифры
def test_create_kit_num_name_get_success_response():
    positive_assert("123")

# Тест 10: Параметр не передан в запросе
def test_create_kit_no_param_name_get_error_response():
    empty_kit_body = data.new_kit_body.copy()
    empty_kit_body.pop("name")
    responce = requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=empty_kit_body,
                         headers=sender_stand_request.new_token())
    assert responce.status_code == 400

# Тест 11: Передан другой тип параметра (число)
def test_create_kit_another_param_name_get_error_response():
    negative_assert(123)