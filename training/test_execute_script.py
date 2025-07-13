"""
Test execute_script method in Selenium.
Command: pytest training\test_execute_script.py
"""

from selenium.webdriver.common.by import By


def test_scroll_to_bottom(browser):
    browser.get('https://parsinger.ru/selenium/6/6.5/index.html')
    btn = browser.find_element(By.ID, 'target')
    browser.execute_script('return arguments[0].scrollIntoView(true)', btn)
    btn.click()
    print(browser.find_element(By.ID, 'secret-key-container').text)
