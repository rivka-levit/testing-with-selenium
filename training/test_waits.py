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
