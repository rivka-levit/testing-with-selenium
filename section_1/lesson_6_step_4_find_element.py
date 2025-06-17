import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)
try:
    # input1 = browser.find_element(By.CSS_SELECTOR, "input:nth-child(1)")
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys('Ivan')
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys('Petrov')
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys('Smolensk')
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys('Russia')
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
except (NoSuchElementException, Exception) as e:
    print(e)
finally:
    time.sleep(30)
    browser.quit()
