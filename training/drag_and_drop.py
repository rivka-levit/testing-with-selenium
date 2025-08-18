"""
Test moving elements on the page.
Command: pytest training\drag_and_drop.py
"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import time


def test_moving_blocks(browser):
    browser.get('https://parsinger.ru/draganddrop/1/index.html')
    block_to_move = browser.find_element(By.ID, 'draggable')
    target = browser.find_element(By.ID, 'field2')
    ActionChains(browser).drag_and_drop(block_to_move, target).perform()
    time.sleep(2)
    print(browser.find_element(By.ID, 'result').text)
