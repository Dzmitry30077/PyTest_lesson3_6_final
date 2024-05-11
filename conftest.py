import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    user_lang = request.config.getoption("language")
    if user_lang:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_lang})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--You need to choose language")
    yield browser
    print("\nquit browser..")
    browser.quit()