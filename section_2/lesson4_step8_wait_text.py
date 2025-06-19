from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # noqa

from section_2.lesson1_step5_click_checkbox import calc

import time


def get_lower_price(browser: webdriver.Chrome, href: str) -> None:
    try:
        browser.get(href)
        WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '100'),
            'Time was out!'
        )
        browser.find_element(By.ID, 'book').click()

        x = int(browser.find_element(By.ID, 'input_value').text)
        browser.find_element(By.ID, 'answer').send_keys(str(calc(x)))
        browser.find_element(By.ID, 'solve').click()

    except (NoSuchElementException, Exception) as e:
        print(e)

    finally:
        time.sleep(20)
        browser.quit()


if __name__ == '__main__':
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    drv = webdriver.Chrome()
    get_lower_price(drv, link)
