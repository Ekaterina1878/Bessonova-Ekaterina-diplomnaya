# Diplom-Chitay-gorod

Автотесты для сайта "Читай-город"

Проект автоматизирует тестирование сайта поиска и покупки книг 
"https://www.chitai-gorod.ru" с помощью UI и API тестов.

Для корректной работы коллекции необходимо в файле settings.py указать актуальный токен. Получить его можно, используя DevTools:
- зайти на сайт интернет-магазина "Читай-город",
- DevTools перейти на вкладку в Application, далее - Storage - Cookies,
выбрать https://www.chitai-gorod.ru,
- в части "Name" найти "access-token",
- внизу поставить галочку в чек-боксе "Show URL-decoded",
- скопировать значение вместе со словом "Bearer",
- вставить его в файл settings.py в поле "access_token".
Также необходимо в файле settings.py в заголовках headers прописать: User-agent и Content-Type. Для этого в  DevTools во вкладке Network перейти на вкладку Headers,
- в поле Response Headers найти Content-type
- скопировать значение application/json;
- вставить в файл settings.py в поле headres в строке Content-type.
- поле Request Headers найти User-agent
- скопировать полностью значение
- вставить его в файл settings.py в поле headers в строке User-agent.

В рамках проекта реализованы:
- UI тесты поиска книг по автору, по названию и по жанру, добавление книги в корзину и выбор книг на странице "Распродажа".
- API тесты запроса поиска книг по автору на кирилице, запрос поиска книг по названию на латинице, запрос поиска книг по жанру, запрос поиска книг по слишком длинному названию, запрос поиска книг с использованием недопустимых символов (смайликов).

 Подготовка окружения
Клонировать проект:
git clone <ссылка-на-репозиторий>
cd project

Создать виртуальное окружение и активировать его:
python -m venv venv
venv\Scripts\activate          # Windows

Установить зависимости:
pip install -r requirements.txt
 
Запуск тестов

UI тесты:
pytest test_ui.py --alluredir=allure-results

API тесты:
pytest test_api.py --alluredir=allure-results

Все тесты:
pytest --alluredir=allure-results


Просмотр Allure отчёта

Сформировать результаты:
pytest --alluredir=allure-results

Запустить сервер Allure:
allure serve allure-results

Примечания

UI тесты используют для стабильности:
- явные ожидания WebDriverWait вместо time.sleep()

API тесты используют библиотеку requests.

Проект поддерживает повторяемость тестов — можно запускать 10+ раз подряд без изменения кода.