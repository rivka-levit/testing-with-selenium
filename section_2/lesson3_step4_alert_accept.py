from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from section_2.lesson1_step5_click_checkbox import calc

import time


def accept_alert(driver: webdriver.Chrome, href: str) -> None:
    try:
        driver.get(href)
        btn = driver.find_element(By.CSS_SELECTOR, 'button.btn')
        btn.click()

        alert = driver.switch_to.alert
        alert.accept()

        x = int(driver.find_element(By.ID, 'input_value').text)
        result = calc(x)

        answer = driver.find_element(By.ID, 'answer')
        answer.send_keys(str(result))

        btn_submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
        btn_submit.click()

    except (NoSuchElementException, Exception) as e:
        print(e)

    finally:
        time.sleep(20)
        driver.quit()


if __name__ == "__main__":
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    accept_alert(browser, link)
