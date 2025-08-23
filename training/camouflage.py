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

    with webdriver.Chrome(options=options) as browser:
        browser.get('https://parsinger.ru/selenium/stealth/1/index.html')
        browser.find_element(By.ID, 'verification-input').send_keys(v_code)
        browser.find_element(By.ID, 'check-button').click()
        secret = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.ID, 'secret'))
        ).text
        print(secret)


def test_hide_chromedriver_one_pass(browser):
    browser.get('https://parsinger.ru/selenium/stealth/1/index.html')
    v_code = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'verification-code'))
    ).text

    browser.execute_script(
        "Object.defineProperty(Navigator.prototype, 'webdriver', {value: false});"
    )
    browser.find_element(By.ID, 'verification-input').send_keys(v_code)
    browser.find_element(By.ID, 'check-button').click()
    secret = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'secret'))
    ).text
    print(secret)


def test_hide_headless_example():
    url = "https://bot.sannysoft.com"
    options = ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless=new")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    )
    # options.add_argument("user-data-dir=c:\\Users\\julia\\AppData\\Local"
    #                      "\\Google\\Chrome\\User Data\\Default"
    #                      )

    with webdriver.Chrome(options=options) as browser:
        filename = "full_page.png"
        total_width = browser.execute_script("return document.documentElement.scrollWidth")
        total_height = browser.execute_script("return document.documentElement.scrollHeight")

        browser.get(url)
        browser.set_window_size(total_width, total_height)
        browser.save_screenshot(filename)
