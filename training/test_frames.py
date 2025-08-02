"""
Test work with frames in a tab.
Command: pytest training\test_frames.py
"""

import time
import re

from selenium.webdriver.common.by import By


def test_work_with_frames(browser):
    browser.get('https://parsinger.ru/selenium/8/8.4.1/')
    frame = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(frame)
    time.sleep(.2)
    letters = re.findall(r'(?<=\*)\w(?=\*)', browser.page_source)
    print(''.join(letters))
