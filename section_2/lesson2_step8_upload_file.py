from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import os
import time


def upload_file(driver: webdriver.Chrome, href: str) -> None:
    try:
        driver.get(href)
        first_name = driver.find_element(By.NAME, 'firstname')
        first_name.send_keys('Sam')
        last_name = driver.find_element(By.NAME, 'lastname')
        last_name.send_keys('Patterson')
        email = driver.find_element(By.NAME, 'email')
        email.send_keys('sam@example.com')

        upload_dir = os.path.join(
            os.path.abspath(os.path.dirname('files')),
            'files'
        )
        file_path = os.path.join(upload_dir, 'file.txt')
        upload_field = driver.find_element(By.ID, 'file')
        upload_field.send_keys(file_path)

        btn = driver.find_element(By.CSS_SELECTOR, 'button.btn')
        btn.click()

    except (NoSuchElementException, Exception) as e:
        print(e)

    finally:
        time.sleep(20)
        driver.quit()


if __name__ == '__main__':
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    upload_file(browser, link)
