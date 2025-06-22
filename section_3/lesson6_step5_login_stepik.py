import pytest
import math
import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # noqa

from dotenv import load_dotenv

load_dotenv()


@pytest.mark.parametrize(
    'url',
    ['https://stepik.org/lesson/236895/step/1',
     'https://stepik.org/lesson/236896/step/1',
     'https://stepik.org/lesson/236897/step/1',
     'https://stepik.org/lesson/236898/step/1',
     'https://stepik.org/lesson/236899/step/1',
     'https://stepik.org/lesson/236903/step/1',
     'https://stepik.org/lesson/236904/step/1',
     'https://stepik.org/lesson/236905/step/1']
)
def test_stepik_solve_problem_success(browser, url):
    """Test solving problem on stepik.org successfully."""

    browser.get(url)
    browser.implicitly_wait(5)

    # Log in to the site

    browser.find_element(By.ID, 'ember479').click()  # Login button
    browser.find_element(By.ID, 'id_login_email').send_keys(
        os.environ.get('STEPIK_USERNAME')
    )
    browser.find_element(By.ID, 'id_login_password').send_keys(
        os.environ.get('STEPIK_PASSWORD')
    )
    browser.find_element(By.CSS_SELECTOR, '#login_form button').click()
    WebDriverWait(browser, 5).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, '.modal-dialog-inner')),
        'Modal window is steal visible.'
    )

    answer = math.log(int(time.time()))

    # Check the textarea is empty. If not - reload the task and fill the field.

    text_area = browser.find_element(
        By.CSS_SELECTOR,
        'textarea[placeholder="Напишите ваш ответ здесь..."]'
    )
    browser.implicitly_wait(10)

    if text_area.is_enabled():
        text_area.send_keys(str(answer))
    else:
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.again-btn')))
        btn = browser.find_element(By.CSS_SELECTOR, '.again-btn')
        btn.click()

        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            'textarea[placeholder="Напишите ваш ответ здесь..."]'
        )))
        new_text_area = browser.find_element(
            By.CSS_SELECTOR,
            'textarea[placeholder="Напишите ваш ответ здесь..."]'
        )
        new_text_area.send_keys(str(answer))

    # Submit the answer

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))
    )
    btn = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    btn.click()

    # Extract the text of feed back.

    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'p.smart-hints__hint'))
    )
    res_elem = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint')
    res_text = res_elem.text

    assert res_text == 'Correct!'
