from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from section_2.lesson1_step5_click_checkbox import calc

import time


def fill_click_get_attribute(driver: webdriver, ref: str) -> None:
    try:
        browser.get(link)
        picture = browser.find_element(By.ID, 'treasure')
        x = picture.get_attribute('valuex')
        result = calc(int(x))

        input_field = browser.find_element(By.ID, 'answer')
        input_field.send_keys(str(result))

        checkbox = browser.find_element(By.ID, 'robotCheckbox')
        checkbox.click()

        radio = browser.find_element(By.ID, 'robotsRule')
        radio.click()

        btn = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        btn.click()

    except (NoSuchElementException, Exception) as e:
        print(e)

    finally:
        time.sleep(20)
        browser.quit()


if __name__ == '__main__':
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    fill_click_get_attribute(browser, link)
