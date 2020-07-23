import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from SLGI.Pages.Prices_and_Performance import Prices_and_performance

baseurl = "https://www.sunlifeglobalinvestments.com/Slgi/Prices+and+Performance?vgnLocale=en_CA"


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
def PP_page(driver):
    obj = Prices_and_performance(driver)
    yield obj


@pytest.mark.usefixtures("driver", "PP_page")
class Tests():

    def test_10_verify_url2_titles(self, driver, PP_page):
        PP_page.verify_title()

    def test_11_verify_searching_funds_functions_works(self, PP_page):
        PP_page.show_funds()
        print("completed_searching funds")

    def test_12_verify_fund_names(self, PP_page):
        PP_page.verify_funds()

    def test_13_verify_fund_data(self, PP_page):
        PP_page.verify_fund_data()
