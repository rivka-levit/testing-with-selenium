import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def fill_register_form(driver):
    try:
        input1 = driver.find_element(By.TAG_NAME, "input")
        input1.send_keys('Ivan')
        input2 = driver.find_element(By.NAME, 'last_name')
        input2.send_keys('Petrov')
        input3 = driver.find_element(By.CLASS_NAME, 'city')
        input3.send_keys('Smolensk')
        input4 = driver.find_element(By.ID, 'country')
        input4.send_keys('Russia')
        button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
        button.click()
    except (NoSuchElementException, Exception) as e:
        print(e)
    finally:
        time.sleep(20)
        driver.quit()


if __name__ == '__main__':
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    fill_register_form(browser)
