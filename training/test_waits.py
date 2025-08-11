"""
Test work with implicit and explicit waits.
Command: pytest training\test_waits.py
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException



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
    browser.get('http://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html')
    while True:
        browser.find_element(By.ID, 'searchLink').click()
        try:
            wait = WebDriverWait(browser, 2)
            wait.until(EC.url_contains('qLChv49'))
        except TimeoutException:
            pass
        else:
            browser.find_element(By.ID, 'checkButton').click()
            time.sleep(3)  # Time to see bananas
            print(browser.find_element(By.CSS_SELECTOR, '#result p').text)
            break
