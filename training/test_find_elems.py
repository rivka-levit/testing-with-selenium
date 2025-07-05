"""
Test tasks for finding elements using Selenium.
Command: pytest training\test_find_elems.py
"""

import time

from selenium.webdriver.common.by import By


def test_find_a_attribute(browser):
    browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')
    links = browser.find_elements(By.CSS_SELECTOR, 'a[stormtrooper]')

    cnt = 0
    for elem in links:
        value = elem.get_attribute('stormtrooper')
        if value.isdigit():
            cnt += int(value)

    browser.find_element(By.ID, 'inputNumber').send_keys(str(cnt))
    browser.find_element(By.ID, 'checkBtn').click()
    answer = browser.find_element(By.ID, 'feedbackMessage').text
    print(answer)


def test_cascade_search(browser):
    browser.get('https://parsinger.ru/selenium/3/3.3.1/index.html')
    block = browser.find_element(By.ID, 'parent_id')
    child_elems = block.find_elements(By.CLASS_NAME, 'child_class')
    if child_elems:
        child_elems[0].click()

    pwd = browser.find_element(
            By.CSS_SELECTOR,
            '#parent_id .child_class:first-child'
    ).get_attribute('password')

    print(pwd)


def test_group_elems(browser):
    browser.get('https://parsinger.ru/selenium/3/3.3.2/index.html')
    elems = browser.find_elements(By.CLASS_NAME, 'block')
    for elem in elems:
        elem.find_element(By.CLASS_NAME, 'button').click()

    time.sleep(2)
    print(browser.find_element(By.TAG_NAME, 'password').text)


def test_filling_inputs(browser):
    browser.get('http://parsinger.ru/selenium/1/1.html')
    inputs = browser.find_elements(By.CLASS_NAME, 'form')
    for inp in inputs:
        inp.send_keys('Text')
    browser.find_element(By.ID, 'btn').click()
    time.sleep(10)


def test_find_by_partial_link(browser):
    browser.get('http://parsinger.ru/selenium/2/2.html')
    link = browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624')
    link.click()
    print(browser.find_element(By.ID, 'result').text)
