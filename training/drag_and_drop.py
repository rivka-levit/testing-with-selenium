"""
Test moving elements on the page.
Command: pytest training\drag_and_drop.py
"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.color import Color
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


def test_move_boxes_home(browser):
    browser.get('https://parsinger.ru/selenium/5.10/2/index.html')
    boxes = browser.find_elements(By.CLASS_NAME, 'draganddrop')
    home = browser.find_element(By.CLASS_NAME, 'draganddrop_end')
    actions = ActionChains(browser)

    for box in boxes:
        actions.drag_and_drop(box, home).perform()

    msg = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, 'message'))
    )
    print(msg.text)


def test_move_circle_over_blocks(browser):
    browser.get('https://parsinger.ru/draganddrop/2/index.html')
    circle = browser.find_element(By.ID, 'draggable')
    blocks = browser.find_elements(By.CLASS_NAME, 'box')
    actions = ActionChains(browser)

    for block in blocks:
        actions.drag_and_drop(circle, block).perform()

    actions.move_by_offset(50, 30).release().perform()
    print(browser.find_element(By.ID, 'message').text)


def test_find_color_pair(browser):
    browser.get('https://parsinger.ru/selenium/5.10/3/index.html')
    bricks = browser.find_elements(By.CLASS_NAME, 'draganddrop')
    bases = browser.find_elements(By.CLASS_NAME, 'draganddrop_end')

    # Create dictionary of bricks with rgb color as a key
    color_keys = {Color.from_string(brk.value_of_css_property('background-color')).rgb: brk for brk in bricks}

    actions = ActionChains(browser)

    for base in bases:
        color = Color.from_string(base.value_of_css_property('border-color')).rgb
        brick = color_keys[color]
        actions.drag_and_drop(brick, base).perform()

    print(browser.find_element(By.ID, 'message').text)


def test_move_circles_by_color(browser):
    browser.get('https://parsinger.ru/selenium/5.10/4/index.html')
    browser.fullscreen_window()
    baskets = browser.find_elements(By.CLASS_NAME, 'basket_color')
    circles = browser.find_elements(By.CLASS_NAME, 'ball_color')

    color_baskets = {Color.from_string(bkt.value_of_css_property('background-color')).hex: bkt for bkt in baskets}

    actions = ActionChains(browser)

    for circle in circles:
        color = Color.from_string(circle.value_of_css_property('background-color')).hex
        actions.drag_and_drop(circle, color_baskets[color]).perform()

    print(browser.find_element(By.CLASS_NAME, 'message').text)
