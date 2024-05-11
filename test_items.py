from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)

    # time.sleep(30)

    elements = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")

    assert len(elements) > 0, "add to cart button is not defined"

    