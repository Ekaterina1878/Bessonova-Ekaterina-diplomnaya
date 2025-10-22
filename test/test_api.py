import requests
import pytest
import allure
from settings import BASE_URL, headers
from data import TEST_DATA


@pytest.fixture(scope="module")
def api_client():
    """Фикстура для настройки клиента API."""
    session = requests.Session()
    session.headers.update(headers)
    yield session
    session.close()


@allure.feature("API test")
@allure.story("Поиск книг по автору")
@allure.step("Поиск книг по автору на кирилице")
def test_search_books_by_author(api_client):
    response = api_client.get(
        f"{BASE_URL}/search/product?phrase={TEST_DATA['author_name']}",
        headers=headers)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200


@allure.feature("API test")
@allure.story("Поиск книг по названию")
@allure.step("Поиск книг по названию на латинице")
def test_search_books_by_title(api_client):
    response = api_client.get(
        f"{BASE_URL}/search/product?phrase={TEST_DATA['book_title']}",
        headers=headers)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200


@allure.feature("API test")
@allure.story("Поиск книг")
@allure.step("Поиск книг по жанру")
def test_search_books_by_genre(api_client):
    response = api_client.get(
        f"{BASE_URL}/search/product?phrase={TEST_DATA['genre']}",
        headers=headers)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200


@allure.feature("API test")
@allure.story("Поиск книг по названию")
@allure.step("Поиск книг по слишком длинному названию")
def test_search_books_by_longe_title(api_client):
    response = api_client.get(
        f"{BASE_URL}/search/product?phrase={TEST_DATA['longe_title']}",
        headers=headers)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 422


@allure.feature("API test")
@allure.story("Поиск книг")
@allure.step("Поиск книг c недопустимыми символами")
def test_search_books_by_simbol_smiley(api_client):
    response = api_client.get(
        f"{BASE_URL}/search/product?phrase={TEST_DATA['simbol_smiley']}",
        headers=headers)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 400
