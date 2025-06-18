from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from math import log, sin

import time


def calc(num: int) -> float:
    return log(abs(12 * sin(num)))


link = 'https://suninjuly.github.io/math.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    result = calc(int(x_element.text))

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(str(result))

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radio.click()

    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()

except (NoSuchElementException, Exception) as e:
    print(e)

finally:
    time.sleep(20)
    browser.quit()
