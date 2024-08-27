import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

session = requests.session()

# Налаштування логування
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Обробник для виводу в консоль (INFO і нижче)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# Обробник для запису у файл (WARNING і нижче)
file_handler = logging.FileHandler('test_search.log')
file_handler.setLevel(logging.WARNING)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Додавання обробників до логгера
logger.addHandler(console_handler)
logger.addHandler(file_handler)


# Фікстура для аутентифікації (scope='class')
@pytest.fixture(scope='class')
def auth_token():
    url = 'http://127.0.0.1:8080/auth'
    auth = HTTPBasicAuth('test_user', 'test_pass')
    response = session.post(url, auth=auth)
    assert response.status_code == 200, "Authentication failed"
    token = response.json().get('access_token')
    assert token, "No access token found in response"
    return token


# Параметри для позитивних тестів
@pytest.mark.parametrize("sort_by, limit", [
    ('price', 5),
    ('year', 10),
    ('engine_volume', 3),
    ('price', 1),
    ('year', 7),
    ('engine_volume', 15),
    ('price', 20)
])
def test_search_cars(auth_token, sort_by, limit):
    url = 'http://127.0.0.1:8080/cars'
    headers = {'Authorization': f'Bearer {auth_token}'}
    params = {'sort_by': sort_by, 'limit': limit}

    # Виконання GET запиту
    response = requests.get(url, headers=headers, params=params)

    # Логування запиту та відповіді
    logger.info(f'GET {url} with params: {params}')
    logger.info(f'Response code: {response.status_code}')
    logger.info(f'Response body: {response.json()}')

    # Перевірка статус-коду відповіді
    assert response.status_code == 200, "Search request failed"


# Негативні тести
def test_search_cars_invalid_token():
    url = 'http://127.0.0.1:8080/cars'
    headers = {'Authorization': 'Bearer invalid_token'}
    params = {'sort_by': 'price', 'limit': 5}

    # Виконання GET запиту з неправильним токеном
    response = requests.get(url, headers=headers, params=params)

    # Логування
    logger.warning(f'GET {url} with invalid token')
    logger.warning(f'Response code: {response.status_code}')
    logger.warning(f'Response body: {response.json()}')

    # Перевірка, що запит був відхилений (очікується 401 або 403)
    assert response.status_code in [401, 403], "Request with invalid token should be unauthorized"


def test_search_cars_missing_params(auth_token):
    url = 'http://127.0.0.1:8080/cars'
    headers = {'Authorization': f'Bearer {auth_token}'}

    # Виконання GET запиту без параметрів
    response = requests.get(url, headers=headers)

    # Логування
    logger.warning(f'GET {url} with missing params')
    logger.warning(f'Response code: {response.status_code}')
    logger.warning(f'Response body: {response.json()}')

    # Перевірка, що запит був відхилений або оброблений з помилкою
    assert response.status_code != 200, "Request with missing parameters should not return 200"


def test_search_cars_invalid_params(auth_token):
    url = 'http://127.0.0.1:8080/cars'
    headers = {'Authorization': f'Bearer {auth_token}'}
    params = {'sort_by': 'invalid_param', 'limit': -5}

    # Виконання GET запиту з неправильними параметрами
    response = requests.get(url, headers=headers, params=params)

    # Логування
    logger.warning(f'GET {url} with invalid params: {params}')
    logger.warning(f'Response code: {response.status_code}')
    logger.warning(f'Response body: {response.json()}')

    # Перевірка, що запит був відхилений або оброблений з помилкою
    assert response.status_code != 200, "Request with invalid parameters should not return 200"
