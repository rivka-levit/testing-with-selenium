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


def test_refresh(browser):
    browser.get('https://parsinger.ru/methods/1/index.html')
    result = browser.find_element(By.ID, 'result').text
    while not result.isdigit():
        browser.refresh()
        result = browser.find_element(By.ID, 'result').text
    print(result)


def test_clear_method(browser):
    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')
    fields = browser.find_elements(By.CLASS_NAME, 'text-field')
    for field in fields:
        field.clear()
    browser.find_element(By.ID, 'checkButton').click()
    alert = browser.switch_to.alert
    print(alert.text)


def test_get_attr_method(browser):
    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
    fields = browser.find_elements(By.CLASS_NAME, 'text-field')
    for field in fields:
        if not field.get_attribute('disabled'):
            field.clear()
    browser.find_element(By.ID, 'checkButton').click()
    alert = browser.switch_to.alert
    print(alert.text)


def test_is_selected_method(browser):
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
    blocks = browser.find_elements(By.CLASS_NAME, 'parent')
    result = 0
    for block in blocks:
        if block.find_element(By.CLASS_NAME, 'checkbox').is_selected():
            value = block.find_element(By.TAG_NAME, 'textarea').get_attribute('value')
            result += int(value)
    print(result)


def test_move_value_from_gray_to_blue(browser):
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
    blocks = browser.find_elements(By.CLASS_NAME, 'parent')
    for block in blocks:
        gray_field = block.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]')
        blue_field = block.find_element(By.CSS_SELECTOR, 'textarea[color="blue"]')
        blue_field.send_keys(gray_field.text)
        gray_field.clear()
        block.find_element(By.TAG_NAME, 'button').click()
    browser.find_element(By.ID, 'checkAll').click()
    print(browser.find_element(By.ID, 'congrats').text)
