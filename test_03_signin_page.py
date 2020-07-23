import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from SLGI.Pages.Signin_page import Signin_form

baseurl = "https://www.sunlifeglobalinvestments.com/Slgi/signin/slgiinv/home"


# client sign in
@pytest.fixture(scope='function', autouse=True)
def driver(request):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument(f"--window-size={1920},{3926}")
    # chrome_options.add_argument("--hide-scrollbars")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(8)
    driver.get(baseurl)

    def driver_teardown():
        print("closing browser")
        driver.close()

    request.addfinalizer(driver_teardown)
    yield driver


@pytest.fixture(scope='function', autouse=True)
def signin_form(driver):
    obj = Signin_form(driver)
    yield obj


@pytest.mark.usefixtures("driver", "signin_form")
class Tests():
    def test_14_verify_url3_title(self, signin_form):
        time.sleep(3)
        signin_form.verify_title()

    def test_15_verify_sign_in_text_present_in_header(self, signin_form):
        signin_form.verify_signin_header()

    def test_16_verify_signin_fucntion(self, signin_form):
        signin_form.verify_signin_functionality()

    def test_17_verify_client_text_not_present_in_advisor_sign_in(self, signin_form):
        signin_form.client_text_not_present()

    def test_18_verify_clicking_forgot_access_ID_moves_to_forgot_page(self, signin_form):
        signin_form.verify_forgot_access_ID()

    def test_19_verify_clicking_forgot_password_moves_to_forgot_page(self, signin_form):
        signin_form.verify_forgot_password()

