"""
Script to extract JSON data from web pages using CDP
Command: pytest training\test_network_requests.py
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

import json
import time

"""
Скрипт для извлечения JSON-данных с веб-страниц с использованием CDP
- Автоматически фильтрует только JSON-ответы
- Декодирует данные и преобразует их в Python-объекты
- Сохраняет каждый найденный JSON в отдельный файл
"""

options = Options()
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})


# Функция для фильтрации JSON-ответов
def log_filter(log_):
    return log_["method"] == "Network.responseReceived" and "json" in log_["params"]["response"]["mimeType"]


def get_all_json_requests(driver):

    # Если нужно — можно инициировать события тут, например клик или ввод
    # browser.find_element(...).click()

    # Получаем "сырые" логи производительности (Performance logs)
    logs_raw = driver.get_log("performance")

    # Фильтруем и вытаскиваем полезные JSON-сообщения
    logs = [json.loads(lr["message"])["message"] for lr in logs_raw]

    # Счетчик найденных JSON
    json_count = 0

    print("\n" + "=" * 80)
    print("НАЧАЛО СБОРА JSON-ДАННЫХ")
    print("=" * 80 + "\n")

    # Перебираем отфильтрованные логи (только JSON-ответы)
    for log in filter(log_filter, logs):
        try:
            request_id = log["params"]["requestId"]
            resp_url = log["params"]["response"]["url"]

            json_count += 1
            print("\n" + "=" * 80)
            print(f"JSON #{json_count}")
            print(f"URL: {resp_url}")

            body = driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})

            # Попытка сохранить JSON в файл
            try:
                # После этой строки у вас есть готовый Python-объект json_data, с которым можно выполнять любые операции.
                json_data = json.loads(body['body'])

                # Сохраняем JSON напрямую в директории скрипта
                filename = f"json_{json_count}.json"
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(json_data, f, indent=4, ensure_ascii=False)
                print(f"Сохранено в файл: {filename}")
            except Exception as e:
                print(f"Ошибка при сохранении JSON: {e}")
                # Если не удалось обработать как JSON, сохраняем текст как есть
                fallback_filename = f"raw_response_{json_count}.txt"
                with open(fallback_filename, 'w', encoding='utf-8') as f:
                    f.write(body['body'])
                print(f"Сохранен необработанный ответ в: {fallback_filename}")

        except WebDriverException:
            print('Нет Body для данного запроса')
            continue


def test_script_get_json_requests():
    with webdriver.Chrome(options=options) as browser:
        browser.get("http://31.130.149.237/json_extraction")
        time.sleep(5)
        get_all_json_requests(driver=browser)


def test_get_json_contacts():
    with webdriver.Chrome(options=options) as browser:
        browser.get('http://31.130.149.237/json_extraction')
        time.sleep(5)
        browser.find_element(By.ID, 'contactsButton').click()
        time.sleep(5)
        get_all_json_requests(driver=browser)
