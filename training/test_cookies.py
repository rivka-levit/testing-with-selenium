"""
Test work with cookies in Selenium.
Command: pytest training\test_cookies.py
"""
import time

from selenium.webdriver.common.by import By


def test_get_one_cookie(browser):
    browser.get('https://parsinger.ru/selenium/6/6.3.1/index.html')
    cookie = browser.get_cookie('token_22')
    print(cookie['value'])


def test_get_song_from_cookies(browser):
    browser.get('https://parsinger.ru/selenium/6/6.3/index.html')
    cookies = browser.get_cookies()
    song = cookies[0]['name']
    time.sleep(2)
    browser.find_element(By.ID, 'phraseInput').send_keys(song)
    time.sleep(2)
    browser.find_element(By.ID, 'checkButton').click()
    time.sleep(2)
    print(browser.find_element(By.ID, 'result').text)


def test_delete_cookies(browser):
    browser.get('https://parsinger.ru/selenium/6/6.3.2/index.html')
    browser.delete_all_cookies()
    time.sleep(10)


def test_add_cookies(browser):
    browser.get('https://parsinger.ru/selenium/6/6.3.3/index.html')
    cookie_dict = {
        'name': 'secretKey',    # Любое имя для cookie
        'value': 'selenium123',  # Любое значение для cookie
        # 'expiry': 2_000_000_000,      # Время жизни cookie в секундах
        # 'path': '/',                  # Директория на сервере дял которой будут доступны cookie
        # 'domain': 'parsinger.ru',     # Информация о домене и поддомене для которых доступны cookie
        # 'secure': True,   # or False - Сигнал браузера о том что передать cookie только по защищённому HTTPS
        # 'httpOnly': True,  # or False - Ограничивает доступ к cookie по средствам API
        # 'sameSite': 'Strict',  # or lax or none - Ограничение на передачу cookie между сайтами
    }
    browser.add_cookie(cookie_dict)
    browser.refresh()
    time.sleep(2)
    print(browser.find_element(By.ID, 'password').text)


def test_find_even_cookies(browser):
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    result = 0
    for cookie in cookies:
        cookie_name_number = cookie['name'].split('_')[-1]
        if cookie_name_number.isdigit() and int(cookie_name_number) % 2 == 0:
            result += int(cookie['value'])
    print(result)


def test_cookie_max_expiry(browser):
    browser.get('https://parsinger.ru/methods/5/index.html')
    links = browser.find_elements(By.CSS_SELECTOR, '.urls a')

    max_expiry = 0
    result = None

    for link in links:
        link.click()
        cookies = browser.get_cookies()

        for cookie in cookies:
            expiry = int(cookie['expiry'])
            if expiry > max_expiry:
                max_expiry = expiry
                result = browser.find_element(By.ID, 'result').text

        browser.back()

    print(result)


def test_get_secret_cookies(browser):
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    result = 0

    for cookie in cookies:
        if cookie['name'].startswith('secret_cookie_'):
            result += int(cookie['value'])

    print(result)
