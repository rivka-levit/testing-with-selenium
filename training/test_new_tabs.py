"""
Test work with new tabs and windows.
Command: pytest training\test_new_tabs.py
"""

def test_open_new_tabs(browser):
    browser.get('about:blank')

    browser.switch_to.new_window('tab')
    browser.get('https://parsinger.ru/selenium/8/8.1/site1/')
    num1 = int(''.join([ch for ch in browser.title if ch not in {'4', '3', '9'}]))

    browser.switch_to.new_window('tab')
    browser.get('https://parsinger.ru/selenium/8/8.1/site2/')
    num2 = int(''.join([ch for ch in browser.title if ch not in {'7', '8', '0'}]))

    print(num1 + num2)
