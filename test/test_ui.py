import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.chitai-gorod.ru"
TEST_DATA = {
"search_author": "Булгаков",
"search_title": "Властелин колец",
"search_genre": "фантастика"
}


@pytest.fixture(scope="function")
def driver():
    with allure.step("Открыть вебсайт"):
        driver = webdriver.Chrome()
        driver.get("https://www.chitai-gorod.ru")
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

@allure.feature("Поиск книг")
@allure.story("Поиск книг по автору")
def test_search_books_by_author(driver):
    with allure.step("Открытие вебсайта"):
        driver.get(BASE_URL)

    with allure.step("Найти поле поиска и ввести автора"):
        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "search")))
        search_box.send_keys(TEST_DATA["search_author"])
    
    with allure.step("Нажать на кнопку поиска"):
        driver.find_element(
            By.CSS_SELECTOR,'button.chg-app-button[type="submit"]').click() 

    with allure.step("Ожидание загрузки результатов поиска и их проверка"):
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "search-title__head")))
        result = driver.find_element(By.CLASS_NAME, "search-title__head").text
        expected_text = "Результаты поиска «Булгаков»" 
        assert expected_text.lower() in result.lower(),f"Expected '{
            expected_text}' in '{result}'"

@allure.feature("Поиск книг")
@allure.story("Поиск книг по названию")
def test_search_book_by_title(driver):
    with allure.step("Открытие вебсайта"):
        driver.get(BASE_URL)

    with allure.step("Найти поле поиска и ввести название книги"):
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "search")))
        search_box.send_keys(TEST_DATA["search_title"])

    with allure.step("Нажатие на кнопку поиска"):
        driver.find_element(
            By.CSS_SELECTOR,'button.chg-app-button[type="submit"]').click()

    with allure.step("Ожидание загрузки результатов поиска и их проверка"):
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "search-title__head")))
        result = driver.find_element(By.CLASS_NAME, "search-title__head").text
        expected_text = "Результаты поиска «Властелин колец»" 
        assert expected_text.lower() in result.lower(),f"Expected '{
            expected_text}' in '{result}'"

@allure.feature("Поиск книг")
@allure.story("Поиск книг по жанру")
def test_search_books_by_genre(driver):
    with allure.step("Открытие вебсайта"):
        driver.get(BASE_URL)

    with allure.step("Найти поле поиска и ввести название жанра"):
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "search")))
        search_box.send_keys(TEST_DATA["search_genre"])

    with allure.step("Нажатие на кнопку поиска"):
        driver.find_element(
            By.CSS_SELECTOR,'button.chg-app-button[type="submit"]').click()

    with allure.step("Ожидание загрузки результатов поиска и их проверка"):
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "search-title__head")))
        result = driver.find_element(By.CLASS_NAME, "search-title__head").text
        expected_text = "Результаты поиска «Фантастика»" 
        assert expected_text.lower() in result.lower(),f"Expected '{
            expected_text}' in '{result}'"

@allure.feature("Выбор книг")
@allure.story("Добавление книги в корзину")
def test_add_book_to_cart(driver):
    with allure.step("Открытие вебсайта"):
        driver.get(BASE_URL)

    with allure.step("Найти поле поиска и ввести название книги"):
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "search")))
        search_box.send_keys(TEST_DATA["search_title"])

    with allure.step("Нажатие на кнопку поиска"):
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,'button.chg-app-button[type="submit"]'))).click()

    with allure.step("Ожидание загрузки результатов поиска"):
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "search-title__head")))

    with allure.step("Ожидание для кнопок 'Купить'"):
        buy_buttons = WebDriverWait(driver, 40).until(
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
            EC.element_to_be_clickable(button_to_click))
        button_to_click.click()

    with allure.step("Ожидание и проверка добавления книги в корзину"):
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, "div.chg-indicator")))
    with allure.step("Проверка, что индикатор отображается"):
        indicator = driver.find_element(By.CSS_SELECTOR, "div.chg-indicator")
        assert indicator.is_displayed(), "Индикатор добавления в корзину не отображается."

@allure.feature("Поиск книг")
@allure.story("Выбор книги на странице Распродажа")
def test_select_book_from_sale(driver):
    with allure.step("Открытие главной страницы"):
        driver.get(BASE_URL)
    
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
        buy_buttons = WebDriverWait(driver, 40).until(
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
            EC.element_to_be_clickable(button_to_click))
        button_to_click.click()
    
    with allure.step("Проверка наличия книг на странице распродажи"):
        books = driver.find_elements(By.CLASS_NAME, "product-card")
        assert len(books) > 0,"На странице распродажи не найдено ни одной книги."
