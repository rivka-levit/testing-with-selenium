from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from section_2.lesson1_step5_click_checkbox import calc

import time


def switch_and_calc(browser: webdriver.Chrome, href: str) -> None:
    try:
        browser.get(href)
        browser.find_element(By.CSS_SELECTOR, 'button.trollface.btn').click()
        browser.switch_to.window(browser.window_handles[1])

        x = int(browser.find_element(By.ID, 'input_value').text)

        browser.find_element(By.ID, 'answer').send_keys(str(calc(x)))
        browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    except (NoSuchElementException, Exception) as e:
        print(e)

    finally:
        time.sleep(20)
        browser.quit()


if __name__ == '__main__':
    link = 'http://suninjuly.github.io/redirect_accept.html'
    driver = webdriver.Chrome()
    switch_and_calc(driver, link)
