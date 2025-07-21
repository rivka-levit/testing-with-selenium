"""
Test work with cookies in Selenium.
Command: pytest training\test_action_chains.py
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_drag_and_drop_by_offset(browser):
    browser.get('http://parsinger.ru/selenium/7/7.3.1/index.html')
    peter = browser.find_element(By.ID, 'draggable')
    actions = ActionChains(browser)
    actions.drag_and_drop_by_offset(peter, 0, -200).perform()
    print(browser.find_element(By.ID, 'password').text)


def test_double_click(browser):
    browser.get('https://parsinger.ru/selenium/7/7.3.2/index.html')
    element = browser.find_element(By.ID, 'dblclick-area')
    ActionChains(browser).double_click(element).perform()
    print(browser.find_element(By.ID, 'password').text)
