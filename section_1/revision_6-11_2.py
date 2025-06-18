from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Импортируем WebDriverWait и Expected Conditions для явных ожиданий
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Ссылка для успешного прохождения теста
    link = "http://suninjuly.github.io/registration1.html"

    # Раскомментируйте строку ниже, чтобы проверить падение теста на второй странице
    # link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # --- КЛЮЧЕВОЕ ИЗМЕНЕНИЕ: ИСПОЛЬЗУЕМ УНИКАЛЬНЫЕ И ТОЧНЫЕ СЕЛЕКТОРЫ ---
    # Мы ищем поля внутри первого блока (<div class="first_block">),
    # так как именно в его структуре кроется различие между страницами.

    # Находим поле "First name"
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    first_name.send_keys("Ivan")

    # Находим поле "Last name"
    # Этот селектор сработает на первой странице, но на второй вызовет ошибку
    # NoSuchElementException, потому что там этого поля нет в .first_block
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    last_name.send_keys("Petrov")

    # Находим поле "Email"
    email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    email.send_keys("ivan.petrov@example.com")

    # Находим и нажимаем кнопку отправки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что регистрация прошла успешно
    # Ждем появления элемента с текстом приветствия
    welcome_text_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    # Получаем текст из этого элемента
    welcome_text = welcome_text_element.text

    # Проверяем с помощью assert, что текст соответствует ожидаемому
    assert "Congratulations! You have successfully registered!" == welcome_text
    print("Тест успешно пройден!")

finally:
    # Даем 10 секунд, чтобы визуально оценить результат
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
