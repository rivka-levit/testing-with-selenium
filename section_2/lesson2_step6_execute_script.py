from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from section_2.lesson1_step5_click_checkbox import calc

import time


def page_bot(driver: webdriver.Chrome, href: str) -> None:
    try:
        driver.get(href)

        x = int(driver.find_element(By.ID, 'input_value').text)
        result = calc(x)

        result_field = driver.find_element(By.ID, 'answer')
        result_field.send_keys(str(result))

        check_box = driver.find_element(By.ID, 'robotCheckbox')
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        check_box.click()

        radio = driver.find_element(By.ID, 'robotsRule')
        radio.click()

        btn = driver.find_element(By.CSS_SELECTOR, 'button.btn')
        btn.click()

    except (NoSuchElementException, Exception) as e:
        print(e)

    finally:
        time.sleep(20)
        driver.quit()


link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
page_bot(browser, link)
