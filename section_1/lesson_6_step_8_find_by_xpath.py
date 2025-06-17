import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def fill_register_form(driver):
    try:
        input1 = driver.find_element(By.TAG_NAME, "input")
        input1.send_keys('John')
        input2 = driver.find_element(By.NAME, 'last_name')
        input2.send_keys('Smith')
        input3 = driver.find_element(By.CLASS_NAME, 'city')
        input3.send_keys('New York')
        input4 = driver.find_element(By.ID, 'country')
        input4.send_keys('USA')
        button = driver.find_element(
            By.XPATH, '//form/div[last()]/button[text()="Submit"]'
        )
        button.click()
    except (NoSuchElementException, Exception) as e:
        print(e)
    finally:
        time.sleep(20)
        driver.quit()


if __name__ == '__main__':
    link = "http://suninjuly.github.io/find_xpath_form"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    fill_register_form(browser)
