"""
Test work with cookies in Selenium.
Command: pytest training\test_scrolling.py
"""

import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_scrolling(browser):
    browser.get('https://parsinger.ru/selenium/7/7.1/index.html')
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    print(browser.find_element(By.ID, 'secret-container').text)


def test_scroll_by_arrow_down(browser):
    browser.get('https://parsinger.ru/selenium/7/7.2/index.html')
    input_fields = set()

    while True:
        fields = set(browser.find_elements(By.CLASS_NAME, 'interactive'))
        new_fields = fields.difference(input_fields)

        for field in new_fields:
            input_fields.add(field)
            field.send_keys('abc')
            field.send_keys(Keys.ENTER)
            field.send_keys(Keys.ARROW_DOWN)
            time.sleep(.3)

        try:
            password = browser.find_element(By.ID, 'hidden-password')
        except NoSuchElementException:
            pass
        else:
            print(password.text)
            break
