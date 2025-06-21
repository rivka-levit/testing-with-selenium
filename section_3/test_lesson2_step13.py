import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


class TestUniqueSelectors(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_register1_success(self):
        """Register success on the first page."""

        self.browser.get('http://suninjuly.github.io/registration1.html')
        # Ваш код, который заполняет обязательные поля
        first_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("John")
        last_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("Doe")
        email = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        email.send_keys("example@example.com")

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем загрузки страницы
        self.browser.implicitly_wait(2)

        # Находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")

        # Записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_text, expected_text)

    def test_register2_fails(self):
        """Register raises error on the second page."""

        self.browser.get('http://suninjuly.github.io/registration2.html')

        with self.assertRaises(NoSuchElementException):
            self.browser.find_element(
                By.CSS_SELECTOR,
                ".first_block .first"
            ).send_keys("John")  # Insert first name

            self.browser.find_element(
                By.CSS_SELECTOR,
                ".first_block .second"
            ).send_keys("Doe")  # Insert last name
