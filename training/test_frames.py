"""
Test work with frames in a tab.
Command: pytest training\test_frames.py
"""

import time
import re

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException


def test_work_with_frames(browser):
    browser.get('https://parsinger.ru/selenium/8/8.4.1/')
    frame = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(frame)
    time.sleep(.2)
    letters = re.findall(r'(?<=\*)\w(?=\*)', browser.page_source)
    print(''.join(letters))


def test_matrix(browser):
    browser.get('https://parsinger.ru/selenium/8/8.4.2/index.html')
    for i in range(1, 4):
        browser.switch_to.frame(f'frame{i}')
        browser.find_element(By.CLASS_NAME, 'unlock-button').click()
        time.sleep(2)
        browser.switch_to.default_content()
    browser.switch_to.frame('frame4')
    print(browser.find_element(By.TAG_NAME, 'h2').text)


def test_labyrinth_of_frames(browser):
    browser.get('https://parsinger.ru/selenium/8/8.4.3/index.html')

    for i in range(4):
        iframe = browser.find_element(By.TAG_NAME, 'iframe')
        browser.switch_to.frame(iframe)
        time.sleep(1)
        browser.find_element(By.CLASS_NAME, 'button').click()

    print(browser.find_element(By.CLASS_NAME, 'password-container').text)


def test_codes_from_frames(browser):
    browser.get('https://parsinger.ru/selenium/5.8/5/index.html')
    frames = browser.find_elements(By.CSS_SELECTOR, '#main_container iframe')

    for frame in frames:
        browser.switch_to.frame(frame)
        browser.find_element(By.TAG_NAME, 'button').click()
        time.sleep(.02)
        number = browser.find_element(By.ID, 'numberDisplay').text
        browser.switch_to.default_content()
        guess_input = browser.find_element(By.ID, 'guessInput')
        guess_input.clear()
        guess_input.send_keys(number)
        browser.find_element(By.ID, 'checkBtn').click()
        time.sleep(.1)
        try:
            alert = browser.switch_to.alert
        except NoAlertPresentException:
            pass
        else:
            print(alert.text)
            alert.accept()
            break
