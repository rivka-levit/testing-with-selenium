from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("John")
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("Doe")
    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email.send_keys("example@example.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждем загрузки страницы
    time.sleep(1)

    # Находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    # Записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # Проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    print("Successfully registered!")

except NoSuchElementException:
    print('Test failed!')

finally:
    time.sleep(10)
    browser.quit()
