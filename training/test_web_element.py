"""
Test work with elements in Selenium.
Command: pytest training\test_web_element.py
"""

import time

from selenium.webdriver.common.by import By


def test_start_btn_clicked(browser):
    browser.get('https://parsinger.ru/selenium/3/3.2.1/index.html')
    browser.find_element(By.ID, 'clickButton').click()
    time.sleep(15)


def test_send_keys(browser):
    browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
    browser.find_element(By.ID, 'codeInput').send_keys('Дрогон')
    browser.find_element(By.ID, 'clickButton').click()
    time.sleep(15)


def test_get_text(browser):
    browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
    browser.find_element(By.ID, 'showTextBtn').click()
    text = browser.find_element(By.ID, 'text1').text
    browser.find_element(By.ID, 'userInput').send_keys(text)
    browser.find_element(By.ID, 'checkBtn').click()
    answer = browser.find_element(By.ID, 'text2').text
    print(answer)


def test_get_attribute(browser):
    browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
    browser.find_element(By.ID, 'secret-key-button').click()
    answer = browser.find_element(By.ID, 'secret-key-button')
    print(answer.get_attribute('data'))


def test_play_hex_attribute(browser):
    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
    blocks = browser.find_elements(By.CSS_SELECTOR, '#main-container > div')
    for block in blocks:
        color = block.find_element(By.TAG_NAME, 'span').text
        block.find_element(By.CSS_SELECTOR, f'select > option[value="{color}"]').click()
        block.find_element(By.CSS_SELECTOR, f'div > button[data-hex="{color}"]').click()
        block.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
        block.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(color)
        block.find_element(By.XPATH, './/button[text()="Проверить"]').click()
    browser.find_element(By.XPATH, '//button[text()="Проверить все элементы"]').click()
    alert = browser.switch_to.alert
    print(alert.text)


def test_find_nums_by_checkboxes(browser):
    browser.get('http://parsinger.ru/scroll/2/index.html')
    result = 0
    for i in range(1, 101):
        browser.find_element(By.ID, f'{i}').click()
        number = browser.find_element(By.ID, f'result{i}').text.strip()
        if number:
            result += int(number)
    print(result)


def test_find_uranium_elements(browser):
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    pieces = browser.find_elements(By.CLASS_NAME, 'clickMe')
    for piece in pieces:
        browser.execute_script('return arguments[0].scrollIntoView();', piece)
        piece.click()
    time.sleep(.5)
    print(browser.switch_to.alert.text)
