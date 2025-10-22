import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import URL
from data import TEST_DATA


@pytest.fixture(scope="function")
def driver():
    with allure.step("Открыть вебсайт"):
        driver = webdriver.Chrome()
        driver.get("https://www.chitai-gorod.ru")
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()


@allure.feature("UI test")
@allure.story("Поиск книг по автору")
@allure.step("Поиск книг по автору на кирилице")
def test_search_books_by_author(driver):
    with allure.step("Открытие вебсайта"):
        driver.get(URL)

    with allure.step("Найти поле поиска и ввести автора"):
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "search")))
        search_box.send_keys(TEST_DATA["search_author"])

    with allure.step("Нажать на кнопку поиска"):
        driver.find_element(
            By.CSS_SELECTOR, 'button.chg-app-button[type="submit"]').click()

    with allure.step("Ожидание загрузки результатов поиска и их проверка"):
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "search-title__head")))
        result = driver.find_element(
            By.CLASS_NAME, "search-title__head").text
        expected_text = "Результаты поиска «Булгаков»"
        assert expected_text.lower() in result.lower(), f"Expected '{
            expected_text}' in '{result}'"


@allure.feature("UI test")
@allure.story("Поиск книг по названию")
@allure.step("Поиск книг с цифрами в названии ")
def test_search_book_by_title(driver):
    with allure.step("Открытие вебсайта"):
        driver.get(URL)

    with allure.step("Найти поле поиска и ввести название книги"):
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "search")))
        search_box.send_keys(TEST_DATA["search_title"])

    with allure.step("Нажатие на кнопку поиска"):
        driver.find_element(
            By.CSS_SELECTOR, 'button.chg-app-button[type="submit"]').click()

    with allure.step("Ожидание загрузки результатов поиска и их проверка"):
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "search-title__head")))
        result = driver.find_element(
            By.CLASS_NAME, "search-title__head").text
        expected_text = "1812"
        assert expected_text.lower() in result.lower(), f"Expected '{
            expected_text}' in '{result}'"


@allure.feature("UI test")
@allure.story("Поиск книг по жанру")
@allure.step("Поиск книг по жанру на кирилице")
def test_search_books_by_genre(driver):
    with allure.step("Открытие вебсайта"):
        driver.get(URL)

    with allure.step("Найти поле поиска и ввести название жанра"):
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "search")))
        search_box.send_keys(TEST_DATA["search_genre"])

    with allure.step("Нажатие на кнопку поиска"):
        driver.find_element(
            By.CSS_SELECTOR, 'button.chg-app-button[type="submit"]').click()

    with allure.step("Ожидание загрузки результатов поиска и их проверка"):
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "search-title__head")))
        result = driver.find_element(By.CLASS_NAME, "search-title__head").text
        expected_text = "Результаты поиска «Фантастика»"
        assert expected_text.lower() in result.lower(), f"Expected '{
            expected_text}' in '{result}'"


@allure.feature("UI test")
@allure.story("Поиск книг с коротким названием")
def test_negative_search_book_by_short_title(driver):
    with allure.step("Открытие вебсайта"):
        driver.get(URL)

    with allure.step("Найти поле поиска и ввести название книги"):
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "search")))
        search_box.send_keys(TEST_DATA["short_title"])

    with allure.step("Нажатие на кнопку поиска"):
        driver.find_element(
            By.CSS_SELECTOR, 'button.chg-app-button[type="submit"]').click()

    with allure.step("Ожидание загрузки результатов поиска и их проверка"):
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "search-title__head")))
        result = driver.find_element(By.CLASS_NAME, "search-title__head").text
        expected_text = "Результаты поиска «W»"
        assert expected_text.lower() in result.lower(), f"Expected '{
            expected_text}' in '{result}'"


@allure.feature("UI test")
@allure.story("Выбор книги на странице Распродажа")
def test_select_book_from_sale(driver):
    with allure.step("Открытие главной страницы"):
        driver.get(URL)

    with allure.step("Ожидание загрузки главной страницы"):
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "div.app-header__wrapper")))

    with allure.step("Переход на вкладку 'Распродажа'"):
        sale_tab = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR, '.header-menu__link[href="/sales"]')))
        sale_tab.click()

    with allure.step("Ожидание загрузки страницы распродажи"):
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, ("div.global-left-right-indent"))))

    with allure.step("Ожидание для кнопок 'Купить'"):
        buy_buttons = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((
                By.XPATH, "//div[contains(text(),'Купить')]")))

    with allure.step("Выбор кнопки для клика"):
        button_to_click = buy_buttons[1]

    with allure.step("Прокрутка к элементу перед кликом"):
        for _ in range(3):
            driver.execute_script(
                "arguments[0].scrollIntoView();", button_to_click)

    with allure.step("Ожидание для элемента, что видим и доступен для клика"):
        WebDriverWait(driver, 40).until(
            EC.visibility_of(button_to_click))

        WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable(button_to_click))
        button_to_click.click()

    with allure.step("Проверка наличия книг на странице распродажи"):
        books = driver.find_elements(By.CLASS_NAME, "product-card")
        assert (len(books) > 0,
                "На странице распродажи не найдено ни одной книги.")
