import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from SLGI.Pages.RRSPS_Know_your_limits import RRSPS

baseurl = "https://www.sunlifeglobalinvestments.com/Slgi/Insights+and+Resources/Insights/Investor+education/RRSPs+Know+your+limits?vgnLocale=en_CA"


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
def RRSPs(driver):
    obj = RRSPS(driver)
    yield obj


@pytest.mark.usefixtures("driver", "RRSPs")
class Tests():
    def test_26_verify_url5_title(self, RRSPs):
        time.sleep(3)
        RRSPs.verify_title()

    def test_27_verify_header(self, RRSPs):
        time.sleep(1)
        RRSPs.verify_header()

    def test_28_verify_breadcrumb(self, RRSPs):
        RRSPs.verify_active_breadcrumb()

    def test_29_verify_article_header(self, RRSPs):
        RRSPs.verify_article_header()

    def test_30_verify_clicking_on_advisor_tools_and_calculator_leads_to_corresponding_page(self, RRSPs):
        RRSPs.verify_advisor_tools_and_calculators()
