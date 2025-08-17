"""
Test work with implicit and explicit waits.
Command: pytest training\test_waits.py
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.ui import WebDriverWait



def test_explicit_waits(browser):
    browser.get('https://parsinger.ru/selenium/9/9.1.1/index.html')
    wait = WebDriverWait(browser, 13)
    buttons = browser.find_elements(By.CSS_SELECTOR, '.button-container button')

    for btn in buttons:
        wait.until(EC.element_to_be_clickable(btn)).click()

    print(wait.until(EC.presence_of_element_located((By.ID, 'message'))).text)


def test_wait_correct_title(browser):
    browser.get('https://parsinger.ru/selenium/9/9.2.1/index.html')
    browser.find_element(By.ID, 'startScan').click()
    wait = WebDriverWait(browser, 30)
    wait.until(EC.title_is('Access Granted'))
    print(browser.find_element(By.ID, 'passwordValue').text)


def test_implicit_wait_abcd(browser):
    browser.get('http://parsinger.ru/selenium/9/9.3.1/index.html')
    browser.implicitly_wait(7)
    browser.find_element(By.ID, 'startButton').click()
    for _ in range(5):
        btn = browser.find_element(By.ID, 'dynamicButton')
        btn.click()
    print(browser.find_element(By.ID, 'secretPassword').text)


def test_wait_exact_url(browser):
    browser.get('https://parsinger.ru/selenium/9/9.4.3/index.html')
    browser.find_element(By.CSS_SELECTOR, '.button-container a.btn:last-child').click()
    wait = WebDriverWait(browser, 20)
    wait.until(EC.url_to_be('https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure'))
    print(browser.find_element(By.ID, 'password').text)


def test_wait_url_changes(browser):
    browser.get('https://parsinger.ru/selenium/9/9.4.4/index.html')
    browser.find_element(By.CLASS_NAME, 'btn').click()
    url = browser.current_url
    wait = WebDriverWait(browser, 10)
    wait.until(EC.url_changes(url))
    print(browser.find_element(By.ID, 'password').text)


def test_search_bananas(browser):
    """Use EC without waiting."""

    browser.get('http://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html')
    expected = EC.url_contains('qLChv49')

    while not expected(browser):
        browser.find_element(By.ID, 'searchLink').click()

    browser.find_element(By.ID, 'checkButton').click()
    time.sleep(3)  # Time to see bananas
    print(browser.find_element(By.CSS_SELECTOR, '#result p').text)


def test_url_matches(browser):
    browser.get('https://parsinger.ru/selenium/9/9.4.2/index.html')
    expected_final_url = EC.url_contains('index_2')
    pattern = r'https://parsinger\.ru/selenium/9/9\.4\.2/ok/ok_\d+\.html'
    result = 0

    browser.find_element(By.ID, 'startButton').click()

    while not expected_final_url(browser):
        current_url = browser.current_url
        if EC.url_matches(pattern)(browser):
            num = int(browser.find_element(By.CLASS_NAME, 'number').text)
            result += num
        WebDriverWait(browser, 5).until(EC.url_changes(current_url))

    browser.find_element(By.ID, 'sumInput').send_keys(str(result))
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.find_element(By.ID, 'result').text)


def test_presence_of_element(browser):
    browser.get('https://parsinger.ru/selenium/9/9.5.1/index.html')
    number = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'order-number'))
    )
    print(number.text)


def test_visibility_of_element(browser):
    browser.get('https://parsinger.ru/selenium/9/9.5.2/index.html')
    btn = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'ghost-button'))
    )
    btn.click()
    print(browser.find_element(By.ID, 'password-display').text)


def test_visibility_all_elements(browser):
    browser.get('https://parsinger.ru/selenium/9/9.5.3/index.html')
    browser.find_element(By.ID, 'showProducts').click()

    products = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'product'))
    )
    result = sum([int(
        i.find_element(By.CLASS_NAME, 'price').text.lstrip('$')
    ) for i in products])

    browser.find_element(By.ID, 'sumInput').send_keys(str(result))
    browser.find_element(By.ID, 'checkSum').click()
    msg = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'secretMessage'))
    )
    print(msg.text)


def test_currency_exchange(browser):
    browser.get('https://parsinger.ru/selenium/9/9.6.1/index.html')
    WebDriverWait(browser, 60).until(
        EC.text_to_be_present_in_element((By.ID, 'usd-rate'), '75.50 ₽')
    )
    print(browser.find_element(By.ID, 'secret-code').text)


def test_find_recipie(browser):
    browser.get('https://parsinger.ru/selenium/9/9.6.2/index.html')
    browser.find_element(By.ID, 'ask-jaskier').click()
    WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element_value(
            (By.ID, 'recipe_field'),
            'Селениумий'
        )
    )
    result = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'password'))
    )
    print(result.text)


def test_wait_attribute_text(browser):
    browser.get('https://parsinger.ru/selenium/9/9.6.3/index.html')
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element_attribute(
            (By.ID, 'main-image'),
            'src',
            'success'
        )
    )
    browser.find_element(By.ID, 'main-image').click()
    password = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'password'))
    )
    print(password.text)


def test_element_includes_attribute(browser):
    browser.get('https://parsinger.ru/selenium/9/9.6.4/index.html')
    booking_number = browser.find_element(By.ID, 'booking-number').text
    WebDriverWait(browser, 10).until(
        EC.element_attribute_to_include((By.ID, 'booking-number'), 'confirmed')
    )
    browser.find_element(By.ID, 'booking-input').send_keys(booking_number)
    browser.find_element(By.ID, 'check-button').click()
    password = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'password-value'))
    )
    print(password.text)


def test_order_confirm(browser):
    browser.get('https://parsinger.ru/selenium/9/9.7.1/index.html')
    browser.find_element(By.ID, 'address').send_keys('Some Address')
    browser.find_element(By.CSS_SELECTOR, 'option[value="card"]').click()
    btn_confirm = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'submit-order'))
    )
    btn_confirm.click()

    WebDriverWait(browser, 10).until(EC.all_of(
        EC.invisibility_of_element_located((By.ID, 'spinner')),
        EC.presence_of_element_located((By.ID, 'modal'))
    ))
    browser.find_element(By.ID, 'confirm-address').click()
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.ID, 'modal'))
    )
    browser.find_element(By.ID, 'get-code').click()
    print(browser.find_element(By.ID, 'result').text)


def test_staleness_of_element(browser):
    browser.get('https://parsinger.ru/selenium/9/9.7.2/index.html')
    browser.find_element(By.CLASS_NAME, 'search-box').send_keys('test')
    browser.find_element(By.ID, 'search-button').click()
    old_result = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'old-result'))
    )
    WebDriverWait(browser, 10).until(EC.all_of(
        EC.staleness_of(old_result),
        EC.visibility_of_element_located((By.ID, 'new-result'))
    ))
    browser.find_element(By.ID, 'secret-button').click()
    print(browser.find_element(By.ID, 'result').text)


def test_wait_new_window_open(browser):
    browser.get('https://parsinger.ru/selenium/9/9.7.3/index.html')
    browser.find_element(By.ID, 'summonBtn').click()
    WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(5))
    browser.find_element(By.ID, 'passwordBtn').click()

    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    print(alert.text)
    alert.accept()


def test_wait_exact_title(browser):
    browser.get('http://parsinger.ru/expectations/3/index.html')

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'btn'))
    ).click()

    WebDriverWait(browser, 20).until(EC.title_is('345FDG3245SFD'))
    print(browser.find_element(By.ID, 'result').text)


def test_wait_title_contains(browser):
    browser.get('http://parsinger.ru/expectations/4/index.html')
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'btn'))
    ).click()
    WebDriverWait(browser, 30, poll_frequency=0.1).until(EC.title_contains('JK8HQ'))
    print(browser.title)


def test_wait_element_by_class_name(browser):
    browser.get('https://parsinger.ru/expectations/6/index.html')
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'btn'))
    ).click()
    element = WebDriverWait(browser, 30, poll_frequency=0.1).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'BMH21YY'))
    )
    print(element.text)


def test_wait_div_appears(browser):
    browser.get('https://parsinger.ru/selenium/5.9/2/index.html')
    wait = WebDriverWait(browser, 30)
    wait.until(EC.presence_of_element_located((By.ID, 'qQm9y1rk'))).click()
    alert = wait.until(EC.alert_is_present())
    print(alert.text)


def test_wait_certain_ids(browser):
    ids_to_find = {'xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB',
                   'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I', 'jolHZqD1', 'ZM6Ms3tw',
                   '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR'}
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')
    boxes = browser.find_elements(By.CLASS_NAME, 'box')

    for box in boxes:
        box_id = box.get_attribute('id')
        if box_id in ids_to_find:
            WebDriverWait(browser, 20).until(EC.visibility_of(box))
            box.click()
            if alert := EC.alert_is_present()(browser):
                print(alert.text)
                break


def test_wait_banner_disappeared(browser):
    browser.get('https://parsinger.ru/selenium/5.9/4/index.html')
    WebDriverWait(browser, 7).until(
        EC.element_to_be_clickable((By.ID, 'closeBtn'))
    ).click()
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.ID, 'ad'))
    )
    browser.find_element(By.CSS_SELECTOR, '.box button').click()
    print(browser.find_element(By.ID, 'message').text)


def test_wait_ad_closed_text_appears(browser):
    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')
    pieces_code = list()
    buttons = browser.find_elements(By.CLASS_NAME, 'box_button')

    for btn in buttons:
        btn.click()
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, 'ad_window'))
        )
        browser.find_element(By.ID, 'close_ad').click()
        WebDriverWait(browser, 15).until(lambda _: btn.text != '')
        pieces_code.append(btn.text)

    print('-'.join(pieces_code))


def test_catch_flickering_checkbox(browser):
    browser.get('https://parsinger.ru/selenium/5.9/6/index.html')
    WebDriverWait(browser, 10).until(
        EC.element_located_to_be_selected((By.ID, 'myCheckbox'))
    )
    browser.find_element(By.CSS_SELECTOR, '#main_container button').click()
    print(browser.find_element(By.ID, 'result').text)


def test_follow_multiple_flickering_checkboxes(browser):
    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')
    containers = browser.find_elements(By.CLASS_NAME, 'container')
    for container in containers:
        checkbox = container.find_element(By.TAG_NAME, 'input')
        btn = container.find_element(By.TAG_NAME, 'button')
        WebDriverWait(browser, 30).until(EC.element_to_be_selected(checkbox))
        btn.click()
    print(browser.find_element(By.ID, 'result').text)
