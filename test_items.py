import time

from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_cart_button_visible(browser) -> None:
    """Test the button `Add to cart` is visible on the page."""

    browser.get(link)
    time.sleep(15)
    btn = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')

    assert btn.is_displayed()
