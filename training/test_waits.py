"""
Test work with implicit and explicit waits.
Command: pytest training\test_waits.py
"""

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
