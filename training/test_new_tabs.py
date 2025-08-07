"""
Test work with new tabs and windows.
Command: pytest training\test_new_tabs.py
"""

import time

from selenium.webdriver.common.by import By

CHROME_EDGE_WIDTH = 16
CHROME_EDGE_HEIGHT = 147

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]


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


def test_check_window_size(browser):
    browser.get('https://parsinger.ru/selenium/8/8.2.2/index.html')
    answer = sum(browser.get_window_size().values())
    browser.find_element(By.ID, 'answer').send_keys(str(answer))
    time.sleep(.1)
    browser.find_element(By.ID, 'checkBtn').click()
    time.sleep(1)
    print(browser.find_element(By.ID, 'resultMessage').text)


def test_modal_wins(browser):
    browser.get('https://parsinger.ru/selenium/8/8.3.1/index.html')

    browser.find_element(By.ID, 'alertButton').click()
    time.sleep(.1)
    browser.switch_to.alert.accept()

    browser.find_element(By.ID, 'promptButton').click()
    time.sleep(.1)
    prompt = browser.switch_to.alert
    prompt.send_keys('Alert')
    prompt.accept()

    browser.find_element(By.ID, 'confirmButton').click()
    time.sleep(.1)
    browser.switch_to.alert.accept()

    time.sleep(5)
    print(browser.find_element(By.ID, 'secretKey').text)


def test_find_code_alerts(browser):
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
    for btn in buttons:
        btn.click()
        browser.switch_to.alert.accept()
        result = browser.find_element(By.ID, 'result').text
        if result:
            print(result)
            break


def test_find_correct_code_in_alerts(browser):
    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
    for btn in buttons:
        btn.click()
        alert = browser.switch_to.alert
        pin = alert.text
        alert.accept()
        browser.find_element(By.ID, 'input').send_keys(pin)
        browser.find_element(By.ID, 'check').click()
        result = browser.find_element(By.ID, 'result').text
        if result != 'Неверный пин-код':
            print(result)
            break


def test_enter_code_in_alerts(browser):
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
    pins = browser.find_elements(By.CLASS_NAME, 'pin')

    for pin in pins:
        pin_text = pin.text
        browser.find_element(By.ID, 'check').click()

        alert = browser.switch_to.alert
        alert.send_keys(pin_text)
        alert.accept()

        result = browser.find_element(By.ID, 'result').text
        if result != 'Неверный пин-код':
            print(result)
            break


def test_set_tab_size_with_edges(browser):
    browser.get('http://parsinger.ru/window_size/1/')
    browser.set_window_size(571, 702)
    time.sleep(1)
    print(browser.find_element(By.ID, 'result').text)


def test_find_result_in_correct_tab_size(browser):

    def is_found_result(w: int) -> bool:
        for height in window_size_y:
            browser.get('http://parsinger.ru/window_size/2/index.html')
            browser.set_window_size(
                w + CHROME_EDGE_WIDTH,
                height + CHROME_EDGE_HEIGHT
            )
            time.sleep(.1)
            result = browser.find_element(By.ID, 'result').text
            if result:
                print(result)
                return True
        return False

    for width in window_size_x:
        if is_found_result(width):
            break


def test_find_correct_tab_size(browser):

    def is_found_result(w: int) -> bool:
        for height in window_size_y:
            browser.get('http://parsinger.ru/window_size/2/index.html')
            browser.set_window_size(
                w + CHROME_EDGE_WIDTH,
                height + CHROME_EDGE_HEIGHT
            )
            time.sleep(.01)
            if browser.find_element(By.ID, 'result').text:
                return True
        return False

    for width in window_size_x:
        if is_found_result(width):
            size = browser.get_window_size()
            size['width'] = size['width'] - CHROME_EDGE_WIDTH
            size['height'] = size['height'] - CHROME_EDGE_HEIGHT
            print(size)
            break
