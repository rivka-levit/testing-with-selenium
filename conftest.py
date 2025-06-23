import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireFoxOptions


def pytest_addoption(parser):
    """Add command line options to pytest."""

    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default=None,
                     help="Choose default language of the browser")


@pytest.fixture(scope='function')
def browser(request):
    """Returns a selenium webdriver instance, `chrome` or `firefox`"""

    browser_name = request.config.getoption('browser_name')
    browser_language = request.config.getoption('language')

    if browser_name == 'chrome':
        print("\nstart `chrome` browser for test..")

        # Set options
        options = ChromeOptions()

        # Set language preference to the browser
        if browser_language:
            options.add_experimental_option(
                'prefs',
                {'intl.accept_languages': browser_language}
            )

        browser = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        print("\nstart `firefox` browser for test..")

        #Set options
        options = FireFoxOptions()

        # Set language preference to the browser
        if browser_language:
            options.set_preference('intl.accept_languages', browser_language)

        browser = webdriver.Firefox(options=options)

    else:
        raise pytest.UsageError("--browser_name should be `chrome` or `firefox`")

    yield browser

    print("\nquit browser..")
    browser.quit()
