"""
Test work with implicit and explicit waits.
Command: pytest training\test_waits.py
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.ui import WebDriverWait



def test_explicit_waits(browser):
    browser.get('https://parsinger.ru/selenium/9/9.1.1/index.html')
    wait = WebDriverWait(browser, 13)
    buttons = browser.find_elements(By.CSS_SELECTOR, '.button-container button')

    for btn in buttons:
        wait.until(EC.element_to_be_clickable(btn)).click()

    print(wait.until(EC.presence_of_element_located((By.ID, 'message'))).text)


def test_wait_correct_title(browser):
    browser.get('https://parsinger.ru/selenium/9/9.2.1/index.html')
    browser.find_element(By.ID, 'startScan').click()
    wait = WebDriverWait(browser, 30)
    wait.until(EC.title_is('Access Granted'))
    print(browser.find_element(By.ID, 'passwordValue').text)


def test_implicit_wait_abcd(browser):
    browser.get('http://parsinger.ru/selenium/9/9.3.1/index.html')
    browser.implicitly_wait(7)
    browser.find_element(By.ID, 'startButton').click()
    for _ in range(5):
        btn = browser.find_element(By.ID, 'dynamicButton')
        btn.click()
    print(browser.find_element(By.ID, 'secretPassword').text)


def test_wait_exact_url(browser):
    browser.get('https://parsinger.ru/selenium/9/9.4.3/index.html')
    browser.find_element(By.CSS_SELECTOR, '.button-container a.btn:last-child').click()
    wait = WebDriverWait(browser, 20)
    wait.until(EC.url_to_be('https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure'))
    print(browser.find_element(By.ID, 'password').text)


def test_wait_url_changes(browser):
    browser.get('https://parsinger.ru/selenium/9/9.4.4/index.html')
    browser.find_element(By.CLASS_NAME, 'btn').click()
    url = browser.current_url
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_changes(url))
    print(browser.find_element(By.ID, 'password').text)


def test_search_bananas(browser):
    """Use EC without waiting."""

    browser.get('http://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html')
    expected = EC.url_contains('qLChv49')

    while not expected(browser):
        browser.find_element(By.ID, 'searchLink').click()

    browser.find_element(By.ID, 'checkButton').click()
    time.sleep(3)  # Time to see bananas
    print(browser.find_element(By.CSS_SELECTOR, '#result p').text)


def test_url_matches(browser):
    browser.get('https://parsinger.ru/selenium/9/9.4.2/index.html')
    expected_final_url = EC.url_contains('index_2')
    pattern = r'https://parsinger\.ru/selenium/9/9\.4\.2/ok/ok_\d+\.html'
    result = 0

    browser.find_element(By.ID, 'startButton').click()

    while not expected_final_url(browser):
        current_url = browser.current_url
        if EC.url_matches(pattern)(browser):
            num = int(browser.find_element(By.CLASS_NAME, 'number').text)
            result += num
        WebDriverWait(browser, 5).until(EC.url_changes(current_url))

    browser.find_element(By.ID, 'sumInput').send_keys(str(result))
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.find_element(By.ID, 'result').text)


def test_presence_of_element(browser):
    browser.get('https://parsinger.ru/selenium/9/9.5.1/index.html')
    number = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'order-number'))
    )
    print(number.text)


def test_visibility_of_element(browser):
    browser.get('https://parsinger.ru/selenium/9/9.5.2/index.html')
    btn = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'ghost-button'))
    )
    btn.click()
    print(browser.find_element(By.ID, 'password-display').text)


def test_visibility_all_elements(browser):
    browser.get('https://parsinger.ru/selenium/9/9.5.3/index.html')
    browser.find_element(By.ID, 'showProducts').click()

    products = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'product'))
    )
    result = sum([int(
        i.find_element(By.CLASS_NAME, 'price').text.lstrip('$')
    ) for i in products])

    browser.find_element(By.ID, 'sumInput').send_keys(str(result))
    browser.find_element(By.ID, 'checkSum').click()
    msg = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'secretMessage'))
    )
    print(msg.text)


def test_currency_exchange(browser):
    browser.get('https://parsinger.ru/selenium/9/9.6.1/index.html')
    WebDriverWait(browser, 60).until(
        EC.text_to_be_present_in_element((By.ID, 'usd-rate'), '75.50 ₽')
    )
    print(browser.find_element(By.ID, 'secret-code').text)


def test_find_recipie(browser):
    browser.get('https://parsinger.ru/selenium/9/9.6.2/index.html')
    browser.find_element(By.ID, 'ask-jaskier').click()
    WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element_value(
            (By.ID, 'recipe_field'),
            'Селениумий'
        )
    )
    result = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'password'))
    )
    print(result.text)
