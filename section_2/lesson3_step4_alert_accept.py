from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from section_2.lesson1_step5_click_checkbox import calc

import time


def submit_result(driver: webdriver.Chrome, href: str) -> None:
    try:
        driver.get(href)
        driver.find_element(By.CSS_SELECTOR, 'button.btn').click()
        driver.switch_to.alert.accept()

        x = int(driver.find_element(By.ID, 'input_value').text)
        result = calc(x)

        driver.find_element(By.ID, 'answer').send_keys(str(result))
        driver.find_element(By.CSS_SELECTOR, 'button.btn').click()

    except (NoSuchElementException, Exception) as e:
        print(e)

    finally:
        time.sleep(20)
        driver.quit()


if __name__ == "__main__":
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    submit_result(browser, link)
