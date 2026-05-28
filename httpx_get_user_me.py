'''
Практическое задание: работа с HTTPX
В данном задании вам необходимо написать скрипт, который выполнит следующие шаги:
1. Отправит POST-запрос на эндпоинт /api/v1/authentication/login с необходимыми учетными данными и получит accessToken из ответа.
2. Используя полученный accessToken, выполнит GET-запрос к эндпоинту /api/v1/users/me.
    - Важно: токен передается в заголовке запроса Authorization: Bearer <ACCESS_TOKEN>, где <ACCESS_TOKEN> — это полученное на первом шаге значение.
3. Выведет в консоль JSON-ответ от сервера с данными о пользователе и статус код ответа.
'''

import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
get_user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=get_user_headers)
get_user_response_data = get_user_response.json()

# Выводим обновленные токены
print("Get user response:", get_user_response_data)
print("Get user status code:", get_user_response.status_code)
