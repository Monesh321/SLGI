import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from SLGI.Pages.Advisor_tools_and_calculator import Advisor_tools_and_calculator

baseurl = "https://www.sunlifeglobalinvestments.com/Slgi/Insights+and+Resources/Resources/Advisor+tools+and+calculators?vgnLocale=en_CA"


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
def advisor_tools_and_calculator(driver):
    obj = Advisor_tools_and_calculator(driver)
    yield obj


@pytest.mark.usefixtures("driver", "advisor_tools_and_calculator")
class Tests():
    def test_31_verify_url6_title(self, advisor_tools_and_calculator):
        time.sleep(3)
        advisor_tools_and_calculator.verify_title()

    def test_32_verify_header(self, advisor_tools_and_calculator):
        time.sleep(1)
        advisor_tools_and_calculator.verify_header()

    def test_33_verify_breadcrumb(self, advisor_tools_and_calculator):
        advisor_tools_and_calculator.verify_active_breadcrumb()

    def test_34_verify_illustration_tool_pg_opens(self, advisor_tools_and_calculator):
        advisor_tools_and_calculator.verify_illustration_tool_opens()

    def test_35_verify_granite_tool_pg_opens(self, advisor_tools_and_calculator):
        advisor_tools_and_calculator.verify_granite_tool_opens()

    def test_36_verify_series_t_calculator(self, advisor_tools_and_calculator):
        advisor_tools_and_calculator.verify_series_t_cal_tool_opens()

