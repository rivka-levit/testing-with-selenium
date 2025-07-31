"""
Test work with new tabs and windows.
Command: pytest training\test_new_tabs.py
"""

import time

from selenium.webdriver.common.by import By


def test_open_new_tabs(browser):
    browser.get('about:blank')

    browser.switch_to.new_window('tab')
    browser.get('https://parsinger.ru/selenium/8/8.1/site1/')
    num1 = int(''.join([ch for ch in browser.title if ch not in {'4', '3', '9'}]))

    browser.switch_to.new_window('tab')
    browser.get('https://parsinger.ru/selenium/8/8.1/site2/')
    num2 = int(''.join([ch for ch in browser.title if ch not in {'7', '8', '0'}]))

    print(num1 + num2)


def test_switch_to_tabs(browser):
    browser.get('https://parsinger.ru/selenium/8/8.1.2/index.html')
    elements_a = browser.find_elements(By.CSS_SELECTOR, '.code-links a')
    links = [i.get_attribute('href') for i in elements_a]
    result = 0

    for link in links:
        browser.switch_to.new_window('tab')
        browser.get(link)

    time.sleep(3)

    for page in browser.window_handles[1:]:
        browser.switch_to.window(page)
        nums = browser.find_elements(By.CLASS_NAME, 'number')
        result += sum([int(i.text) for i in nums])

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
    browser.find_element(By.ID, 'sumInput').send_keys(str(result))
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.find_element(By.ID, 'passwordDisplay').text)


def test_set_window_size(browser):
    browser.get('https://parsinger.ru/selenium/8/8.2.1/index.html')
    browser.set_window_size(1200, 720)
    time.sleep(1)
    browser.find_element(By.ID, 'checkSizeBtn').click()
    time.sleep(1)
    print(browser.find_element(By.ID,'secret').text)
