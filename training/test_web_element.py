import time

from selenium.webdriver.common.by import By


def test_start_btn_clicked(browser):
    browser.get('https://parsinger.ru/selenium/3/3.2.1/index.html')
    browser.find_element(By.ID, 'clickButton').click()
    time.sleep(15)


def test_send_keys(browser):
    browser.get('https://parsinger.ru/selenium/3/3.2.2/index.html')
    browser.find_element(By.ID, 'codeInput').send_keys('Дрогон')
    browser.find_element(By.ID, 'clickButton').click()
    time.sleep(15)


def test_get_text(browser):
    browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
    browser.find_element(By.ID, 'showTextBtn').click()
    text = browser.find_element(By.ID, 'text1').text
    browser.find_element(By.ID, 'userInput').send_keys(text)
    browser.find_element(By.ID, 'checkBtn').click()
    answer = browser.find_element(By.ID, 'text2').text
    print(answer)


def test_get_attribute(browser):
    browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
    browser.find_element(By.ID, 'secret-key-button').click()
    answer = browser.find_element(By.ID, 'secret-key-button')
    print(answer.get_attribute('data'))
