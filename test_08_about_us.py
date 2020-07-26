import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from SLGI.Pages.About_us import About_us

baseurl = "https://www.sunlifeglobalinvestments.com/Slgi/About+us?vgnLocale=en_CA"


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
def about_us(driver):
    obj = About_us(driver)
    yield obj


@pytest.mark.usefixtures("driver", "about_us")
class Tests():
    def test_46_verify_url8_title(self, about_us):
        time.sleep(3)
        about_us.verify_title()

    def test_47_verify_header(self, about_us):
        time.sleep(1)
        about_us.verify_header()

    def test_48_verify_breadcrumb(self, about_us):
        about_us.verify_active_breadcrumb()

    def test_49_verify_who_we_are_page_opens_on_clicking_btn(self, about_us):
        about_us.move_to_who_we_are_page()

    def test_50_verify_Investment_management_page_opens_on_clicking_btn(self, about_us):
        about_us.move_to_Investment_management_page()

    def test_51_verify_sponsorship_page_opens_on_clicking_btn(self, about_us):
        about_us.move_to_sponsorship_page()
