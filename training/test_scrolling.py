"""
Test work with cookies in Selenium.
Command: pytest training\test_scrolling.py
"""

import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement


def test_scrolling(browser):
    browser.get('https://parsinger.ru/selenium/7/7.1/index.html')
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    print(browser.find_element(By.ID, 'secret-container').text)


def test_scroll_by_arrow_down(browser):
    browser.get('https://parsinger.ru/selenium/7/7.2/index.html')
    input_fields = set()

    while True:
        fields = set(browser.find_elements(By.CLASS_NAME, 'interactive'))
        new_fields = fields.difference(input_fields)

        for field in new_fields:
            input_fields.add(field)
            field.send_keys('abc')
            field.send_keys(Keys.ENTER)
            field.send_keys(Keys.ARROW_DOWN)
            time.sleep(.3)

        try:
            password = browser.find_element(By.ID, 'hidden-password')
        except NoSuchElementException:
            pass
        else:
            print(password.text)
            break


def test_scroll_with_end_key(browser):
    browser.get('https://parsinger.ru/selenium/7/7.3.5/index.html')
    containers = browser.find_elements(By.CLASS_NAME, 'scroll-container')
    actions = ActionChains(browser)

    for container in containers:
        actions.click(container).send_keys(Keys.END).perform()
        # actions.send_keys_to_element(container, Keys.END).perform()
        time.sleep(2)

    print(browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)


def test_scroll_by_amount(browser):
    browser.get('https://parsinger.ru/selenium/7/7.4.1/index.html')
    actions = ActionChains(browser)

    actions.scroll_by_amount(0, 700).perform()
    time.sleep(4)
    code = browser.find_element(By.CLASS_NAME, 'countdown').text.lstrip('Код: ')

    actions.scroll_by_amount(0, 1300).perform()
    time.sleep(2)
    browser.find_element(By.TAG_NAME, 'input').send_keys(code)
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(2)

    final_key = browser.find_element(By.ID, 'final-key').text
    print(final_key.split(' ')[-1])


def test_scroll_to_end_frame(browser):
    browser.get('http://parsinger.ru/infiniti_scroll_2/')
    frame = browser.find_element(By.ID, 'scroll-container')
    actions = ActionChains(browser)
    actions.move_to_element(frame).click().send_keys(Keys.END).perform()
    elements = frame.find_elements(By.TAG_NAME, 'p')
    cnt = 0

    while cnt < len(elements):
        actions.send_keys(Keys.END).perform()
        cnt = len(elements)
        time.sleep(1)
        elements = frame.find_elements(By.TAG_NAME, 'p')

    print(sum([int(i.text) for i in elements]))


def test_infinite_scroll(browser):
    browser.get('http://parsinger.ru/infiniti_scroll_1/')
    frame = browser.find_element(By.ID, 'scroll-container')
    start_boxes = set()
    result = 0
    actions = ActionChains(browser)
    actions.move_to_element(frame).click().send_keys(Keys.END).perform()
    while True:
        boxes = set(frame.find_elements(By.TAG_NAME, 'span'))
        new_boxes = boxes.difference(start_boxes)
        time.sleep(2)
        if new_boxes:
            for box in new_boxes:
                start_boxes.add(box)
                result += int(box.text)
        else:
            break

        actions.send_keys(Keys.END).perform()

    print(result)


def test_scroll_to_end_several_frames(browser):
    browser.get('http://parsinger.ru/infiniti_scroll_3/')
    frames = browser.find_elements(By.XPATH, '//div[contains(@id, "scroll-container")]')
    result = cnt = 0
    actions = ActionChains(browser)

    for frame in frames:
        actions.move_to_element(frame).click().send_keys(Keys.END).perform()
        elements = frame.find_elements(By.TAG_NAME, 'span')

        while cnt < len(elements):
            actions.send_keys(Keys.END).perform()
            cnt = len(elements)
            time.sleep(1)
            elements = frame.find_elements(By.TAG_NAME, 'span')

        result += sum([int(i.text) for i in elements])
        actions.release().perform()
        cnt = 0

    print(result)


def test_even_checkboxes(browser):

    def check_even_checkboxes(container: WebElement) -> None:
        boxes = container.find_elements(By.TAG_NAME, 'input')
        for box in boxes:
            value = int(box.get_attribute('value'))
            if value % 2 == 0:
                box.click()

    browser.get('https://parsinger.ru/selenium/5.7/4/index.html')
    frame = browser.find_element(By.ID, 'main_container')

    actions = ActionChains(browser)
    actions.move_to_element(frame).click().perform()

    start_blocks = set()
    blocks = frame.find_elements(By.CLASS_NAME, 'child_container')
    new_blocks = [i for i in blocks if i not in start_blocks]

    while new_blocks:
        for block in new_blocks:
            check_even_checkboxes(block)
            start_blocks.add(block)
        browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', frame)
        actions.scroll_by_amount(0, 200).perform()
        blocks = frame.find_elements(By.CLASS_NAME, 'child_container')
        new_blocks = [i for i in blocks if i not in start_blocks]

    frame.find_element(By.CLASS_NAME, 'alert_button').click()
    print(browser.switch_to.alert.text)


def test_auto_like_infinite_scroll(browser):

    def get_new_cards_list():
        cards = container.find_elements(By.CLASS_NAME, 'card')
        return [i for i in cards if i not in start_cards]

    browser.get('https://parsinger.ru/selenium/7/7.5/index.html')
    container = browser.find_element(By.ID, 'container')

    actions = ActionChains(browser)
    actions.move_to_element(container).click().perform()

    start_cards = set()
    new_cards = get_new_cards_list()

    result = 0

    while new_cards:
        for card in new_cards:
            start_cards.add(card)
            actions.scroll_to_element(card).perform()
            card.find_element(By.CLASS_NAME, 'like-btn').click()
            time.sleep(.1)
            result += int(card.find_element(By.CLASS_NAME, 'big-number').text)

        browser.execute_script(
            'arguments[0].scrollTop = arguments[0].scrollHeight',
            container
        )
        time.sleep(.1)
        new_cards = get_new_cards_list()

    print(result)
