"""
Test hide using Selenium.
Command: pytest training\camouflage.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.ui import WebDriverWait

import time


def test_hide_webdriver():
    options = ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/stealth/1/index.html')
        v_code = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, 'verification-code'))
        ).text
        print(v_code)
    with webdriver.Chrome(options=options) as browser:
        browser.get('https://parsinger.ru/selenium/stealth/1/index.html')
        browser.find_element(By.ID, 'verification-input').send_keys(v_code)
        browser.find_element(By.ID, 'check-button').click()
        secret = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, 'secret'))
        ).text
        print(secret)
