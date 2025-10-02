# Импорт необходимых модулей
import configuration  # Модуль с настройками URL и путей API
import requests  # Библиотека для выполнения HTTP-запросов
import data  # Модуль с тестовыми данными и телами запросов


# Функция для создания нового пользователя и получения токена
# Выполнение POST-запроса на создание пользователя
# Использование данные пользователя из модуля data
# Возвращение токен из ответа сервера
def get_new_user_token():
    response = requests.post(
        url=configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=data.user_body,  # Тело запроса с данными пользователя
    )
    return response.json()[
        "authToken"
    ]  # Извлечение и возвращение токена авторизации из JSON-ответа


# Функция для создания нового набора
# Выполнение POST-запроса на создание набора
# Добавление заголовков авторизации и типа содержимого
# Защита исходных данных путем создания копии
def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + auth_token,
    }

    # Копирование словаря с телом запроса из переданных данных
    kit_body_copy = kit_body.copy()

    # Выполнение POST-запроса к API для создания нового набора
    return requests.post(
        url=configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
        json=kit_body_copy,
        headers=headers,
    )
