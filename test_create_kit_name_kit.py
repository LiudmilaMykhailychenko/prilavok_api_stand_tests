import sender_stand_request
import data


# Функция для получения тела запроса набора с указанным именем
def get_kit_body(name):
    # Копирование словаря с телом запроса из файла data
    current_body = data.kit_body.copy()
    # Изменение значения в поле name
    current_body["name"] = name
    # Возвращение нового словаря с нужным значением name
    return current_body


# Функция для позитивной проверки
def positive_assert(name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(
        kit_body, sender_stand_request.get_new_user_token()
    )

    # Проверка, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверка, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == name


# Функция для негативной проверки, когда в ответе ошибка
def negative_assert_code_400(kit_body):
    # В переменную response сохраняется результат запроса
    response = sender_stand_request.post_new_client_kit(
        kit_body, sender_stand_request.get_new_user_token()
    )

    # Проверяется, что код ответа равен 400
    assert response.status_code == 400


# Тест 1. Успешное создание набора. Параметр name состоит из 1 символа
def test_create_kit_1_symbol_in_name_get_success_response():
    positive_assert("a")


# Тест 2. Успешное создание набора. Параметр name состоит из 511 символов
def test_create_kit_511_symbols_in_name_get_success_response():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    )


# Тест 3. Ошибка. Параметр name состоит из 0 символов
def test_create_kit_0_symbols_in_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)


# Тест 4. Ошибка. Параметр name состоит из 512 символов
def test_create_kit_512_symbols_in_name_get_error_response():
    kit_body = get_kit_body(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    )
    negative_assert_code_400(kit_body)


# Тест 5. Успешное создание набора. Параметр name состоит из английских букв
def test_create_kit_english_letters_in_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Успешное создание набора. Параметр name состоит из русских букв
def test_create_kit_russian_letters_in_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Успешное создание набора. Параметр name состоит из спецсимволов
def test_create_kit_special_symbols_in_name_get_success_response():
    positive_assert('"№%@"')


# Тест 8. Успешное создание набора. Параметр name состоит из строки с пробелами
def test_create_kit_spaces_in_name_get_success_response():
    positive_assert(" Человек и КО ")


# Тест 9. Успешное создание набора. Параметр name состоит из цифр
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")


# Тест 10. Ошибка. В запросе нет параметра name
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)


# Тест 11. Ошибка. Тип параметра name: число
def test_create_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)
