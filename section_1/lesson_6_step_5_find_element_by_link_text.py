import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from section_1.lesson_6_step_4_find_element import fill_register_form

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()

try:
    browser.get(link)
    time.sleep(1)
    element = browser.find_element(
        By.LINK_TEXT,
        str(math.ceil(math.pow(math.pi, math.e)*10000))
    )
    element.click()
    time.sleep(1)
    fill_register_form(browser)
except (NoSuchElementException, Exception) as e:
    print(e)
finally:
    browser.quit()
