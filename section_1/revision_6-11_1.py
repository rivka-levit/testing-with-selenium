from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # При проверке второй ссылкой надо немного подождать
    link = "http://suninjuly.github.io/registration1.html"
    # link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
    email.send_keys("ivan@example.com")

    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()