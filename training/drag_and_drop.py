"""
Test moving elements on the page.
Command: pytest training\drag_and_drop.py
"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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


def test_send_piece_by_distance(browser):
    browser.get('https://parsinger.ru/selenium/5.10/8/index.html')
    actions = ActionChains(browser)
    pieces = browser.find_elements(By.CLASS_NAME, 'piece')

    for piece in pieces:
        distance = int(piece.get_attribute('id').lstrip('piece_')) + 25
        time.sleep(.1)
        actions.drag_and_drop_by_offset(piece, distance, 0).perform()

    result = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, 'message'))
    )
    print(result.text)


def test_move_sliders_exactly(browser):
    browser.get('https://parsinger.ru/selenium/5.10/6/index.html')
    slider_rows = browser.find_elements(By.CLASS_NAME, 'slider-row')

    for slider in slider_rows:
        current_value = int(
            slider.find_element(By.CLASS_NAME, 'current-value').text
        )
        target_value = int(
            slider.find_element(By.CLASS_NAME, 'target-value').text
        )
        inp = slider.find_element(By.TAG_NAME, 'input')


        while current_value != target_value:
            if current_value < target_value:
                inp.send_keys(Keys.ARROW_RIGHT)
            elif current_value > target_value:
                inp.send_keys(Keys.ARROW_LEFT)
            current_value = int(
                slider.find_element(By.CLASS_NAME, 'current-value').text
            )

    print(
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, 'message'))
        ).text
    )


def test_construct_word(browser):
    browser.get('https://parsinger.ru/draganddrop/4/index.html')
    chars = list(browser.find_element(By.ID, 'target-word').text)
    letter_slots = browser.find_elements(By.CLASS_NAME, 'letter-slot')
    alphabet = browser.find_element(By.ID, 'alphabet')
    actions = ActionChains(browser)

    for ch, slot in zip(chars, letter_slots):
        draggable_char = alphabet.find_element(By.XPATH, f'.//div[text()="{ch}"]')
        actions.drag_and_drop(draggable_char, slot).perform()

    print(
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, 'password'))
        ).text
    )
