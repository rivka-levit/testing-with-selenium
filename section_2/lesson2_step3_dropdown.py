from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import time


def select_sum_from_dropdown(driver: webdriver.Chrome, href: str) -> None:
    try:
        driver.get(href)
        n1 = int(driver.find_element(By.ID, 'num1').text)
        n2 = int(driver.find_element(By.ID, 'num2').text)
        result = n1 + n2
        dropdown = Select(driver.find_element(By.ID, 'dropdown'))
        dropdown.select_by_value(str(result))

        btn = driver.find_element(By.CSS_SELECTOR, 'button.btn')
        btn.click()

    except (NoSuchElementException, Exception) as e:
        print(e)

    finally:
        time.sleep(20)
        driver.quit()


if __name__ == '__main__':
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    select_sum_from_dropdown(browser, link)
