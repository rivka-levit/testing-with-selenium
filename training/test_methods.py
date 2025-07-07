"""
Tasks for testing methods of browser.
Command: pytest training\test_methods.py
"""

from selenium.webdriver.common.by import By


def test_back_method(browser):
    browser.get('https://parsinger.ru/selenium/6/6.2/index.html')
    browser.find_element(By.CSS_SELECTOR, '.container a').click()
    browser.find_element(By.TAG_NAME, 'a').click()
    browser.back()
    browser.back()
    browser.find_element(By.ID, 'getPasswordBtn').click()
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()


def test_screenshot_to_file(browser):
    browser.get('https://parsinger.ru/selenium/6/6.2.1/index.html')
    browser.maximize_window()
    img = browser.find_element(By.ID, 'this_pic')
    img.screenshot('training/images/screenshot.png')
