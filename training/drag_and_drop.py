"""
Test moving elements on the page.
Command: pytest training\drag_and_drop.py
"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.ui import WebDriverWait

import time


def test_moving_blocks(browser):
    browser.get('https://parsinger.ru/draganddrop/1/index.html')
    block_to_move = browser.find_element(By.ID, 'draggable')
    target = browser.find_element(By.ID, 'field2')
    ActionChains(browser).drag_and_drop(block_to_move, target).perform()
    time.sleep(2)
    print(browser.find_element(By.ID, 'result').text)


def test_move_element_by_control_points(browser):
    browser.get('https://parsinger.ru/draganddrop/3/index.html')
    element = browser.find_element(By.ID, 'block1')
    points = browser.find_elements(By.CSS_SELECTOR, 'div.controlPoint')
    actions = ActionChains(browser)
    actions.click_and_hold(element).perform()

    for point in points:
        actions.move_to_element(point).perform()
        time.sleep(.5)

    actions.move_by_offset(30, 0).release().perform()
    msg = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, 'message'))
    )
    print(msg.text)

