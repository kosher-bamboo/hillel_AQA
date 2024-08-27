import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

# logging setting
logger = logging.getLogger('API Test')
logger.setLevel(logging.DEBUG)

# console handler setup
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# file handler setup
file_handler = logging.FileHandler('test_search.log')
file_handler.setLevel(logging.ERROR)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

url = 'http://127.0.0.1:8080/cars'


def log_data(response, params, is_failed):
    logger.info(f'GET {url} with params: {params}')
    if is_failed:
        logger.info(f'Response code: {response.status_code}')
        logger.info(f'Response body items: {len(response.json())}\n')
    else:
        logger.error("Unexpected response")
        logger.error(f'Response code: {response.status_code}')
        logger.error(f'Response body items: {len(response.json())}\n')


# authentification fixture
@pytest.fixture(scope='session')
def session():
    with requests.Session() as session:
        url = 'http://127.0.0.1:8080/auth'
        auth = HTTPBasicAuth('test_user', 'test_pass')
        response = session.post(url, auth=auth)
        if response.status_code != 200:
            pytest.fail("Authentication failed")
        token = response.json().get('access_token')
        if not token:
            pytest.fail("No access token found in response")
        # save token in headers
        session.headers.update({'Authorization': f'Bearer {token}'})
        yield session


# positive tests parameters
@pytest.mark.parametrize("sort_by, limit", [
    ('brand', 5),
    ('year', 10),
    ('engine_volume', 3),
    ('price', 1)
])
def test_search_cars(session, sort_by, limit):
    params = {'sort_by': sort_by, 'limit': limit}
    is_failed = False

    # GET request with parameters
    response = session.get(url, params=params)
    response_data = response.json()

    # logging request and responce
    if len(response_data[0]) == 4:
        is_failed = True
    log_data(response, params, is_failed)

    # compare response length with requested limit
    assert len(response_data) == limit, "Unexpected response"


def test_search_cars_zero_limit(session):
    sort_by = 'brand'
    limit = 0
    params = {'sort_by': sort_by, 'limit': limit}
    is_failed = False

    # GET request with parameters
    response = session.get(url, params=params)
    response_data = response.json()

    # logging request and responce
    if len(response_data) == 0:
        is_failed = True
    log_data(response, params, is_failed)

    # compare response length with reqiested limit
    assert len(response_data) == limit, "Unexpected response"


def test_search_cars_absent_params(session):
    # GET request without parameters
    response = session.get(url)
    response_data = response.json()
    params = {}
    is_failed = False

    # logging request and responce
    if len(response_data[0]) == 4:
        is_failed = True
    log_data(response, params, is_failed)

    # compare response length with requested limit
    assert len(response_data[0]) == 4, "Unexpected response"


# Negative tests
def test_search_cars_invalid_token():
    headers = {'Authorization': 'Bearer invalid_token'}
    params = {'sort_by': 'price', 'limit': 5}
    is_failed = False

    # GET request with invalid token
    response = requests.get(url, headers=headers, params=params)

    # logging request and responce

    if response.status_code == 422:
        is_failed = True
    log_data(response, params, is_failed)

    # check status code
    assert response.status_code == 422, "Request with invalid token should be unauthorized"


# Parametrized negative tests
@pytest.mark.parametrize("invalid_params, expected_status", [
    ({'sort_by': 'invalid_param', 'limit': 5}, 422),  # Неправильний sort_by
    ({'sort_by': 'price', 'limit': -1}, 422),  # Неправильний limit
    ({'sort_by': 'year', 'limit': 'not_a_number'}, 500)  # Невірний формат limit
])
def test_search_cars_invalid_params(session, invalid_params, expected_status):
    # GET request with incorrect parameters
    response = session.get(url, params=invalid_params)
    is_failed = False
    params = {'sort_by': invalid_params, 'limit': expected_status}

    # logging request and responce
    if response.status_code == expected_status:
        is_failed = True
    log_data(response, params, is_failed)

    # Compare response with expected status code
    assert response.status_code == expected_status, f"Request with params {invalid_params} should return {expected_status}"
