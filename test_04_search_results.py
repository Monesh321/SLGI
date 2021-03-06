import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from SLGI.Pages.search_result import search_result

baseurl = "https://www.sunlifeglobalinvestments.com/Slgi/Search+results?q=investment&action=input"


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
def search(driver):
    obj = search_result(driver)
    yield obj


@pytest.mark.usefixtures("driver", "search")
class Tests():
    def test_21_verify_url4_title(self, search):
        time.sleep(3)
        search.verify_title()

    def test_22_verify_search_results_header(self, search):
        search.verify_header_present()

    def test_23_verify_search_results_breadcrumb_is_active(self, search):
        search.verify_breadcrumb_active()

    def test_24_verify_search_results_count_is_displayed_correctly(self, search):
        search.verify_result_count_displayed()

    def test_25_verify_search_results_links_are_valid_urls(self, search):
        search.verify_search_result_links()



