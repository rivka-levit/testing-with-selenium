"""
Test tasks for finding elements using Selenium.
Command: pytest training\test_find_elems.py
"""

import time

from selenium.webdriver.common.by import By

numbers = {1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29, 33, 34, 38,
39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68, 69, 73,
74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114, 118,
119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148, 149, 153,
154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181, 184, 185,
187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205, 206, 207,
208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230, 232, 233,
234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253, 254, 255,
256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288, 289, 291,
292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309, 313, 314,
318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349,
353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409, 411, 412,
419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447, 448, 451,
452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477, 478, 479,
480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513, 514, 518, 519}


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


def test_sum_p_text(browser):
    browser.get('http://parsinger.ru/selenium/3/3.html')
    text_boxes = browser.find_elements(By.TAG_NAME, 'p')
    result = 0
    for box in text_boxes:
        num = box.text
        if num.isdigit():
            result += int(num)
    print(result)


def test_sum_second_p(browser):
    browser.get('http://parsinger.ru/selenium/3/3.html')
    elems = browser.find_elements(By.CSS_SELECTOR, 'div.text p:nth-child(2)')
    print(sum([int(elem.text) for elem in elems]))


def test_click_checkbox(browser):
    browser.get('http://parsinger.ru/selenium/4/4.html')
    boxes = browser.find_elements(By.CLASS_NAME, 'check')
    for box in boxes:
        box.click()
    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)


def test_click_optional_checkbox(browser):
    browser.get('http://parsinger.ru/selenium/5/5.html')
    boxes = browser.find_elements(By.CLASS_NAME, 'check')

    for box in boxes:
        if int(box.get_attribute('value')) in numbers:
            box.click()

    browser.find_element(By.CLASS_NAME, 'btn').click()
    print(browser.find_element(By.ID, 'result').text)
