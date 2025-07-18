"""
Test work with cookies in Selenium.
Command: pytest training\test_scrolling.py
"""

import time

from selenium.webdriver.common.by import By


def test_scrolling(browser):
    browser.get('https://parsinger.ru/selenium/7/7.1/index.html')
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    print(browser.find_element(By.ID, 'secret-container').text)
