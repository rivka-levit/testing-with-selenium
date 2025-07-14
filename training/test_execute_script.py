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


def test_scroll_to_view_element(browser):
    browser.get('http://parsinger.ru/scroll/4/index.html')
    buttons = browser.find_elements(By.CSS_SELECTOR, '.visibility .btn')

    result = 0

    for btn in buttons:
        browser.execute_script('return arguments[0].scrollIntoView(true)', btn)
        btn.click()
        result += int(browser.find_element(By.ID, 'result').text)

    print(result)
