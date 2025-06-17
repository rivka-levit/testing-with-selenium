import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = 'http://suninjuly.github.io/huge_form.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    time.sleep(1)

    inputs = browser.find_elements(By.TAG_NAME, 'input')
    for i in inputs:
        i.send_keys('Мой ответ')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

except (NoSuchElementException, Exception) as e:
    print(e)

finally:
    time.sleep(30)
    browser.quit()
