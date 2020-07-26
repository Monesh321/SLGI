import time
from urllib.parse import urlparse

homeurl = "https://www.sunlifeglobalinvestments.com/"


class Advisor_tools_and_calculator():
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "header_text": "//div[@class='title-bar']//h1[contains(text(),'Advisor tools and calculators')]",
        "active_breadcrumb": "//ol[@class='breadcrumb']//li[@class='active']//span[contains(text(),'Advisor tools and calculators')]",
        "launch_illustration_tool": "//a[contains(text(),'Launch Illustration tool')]",
        "launch_granite_tool": "//a[contains(text(),'Launch Granite tool')]",
        "launch_series_t_calculator": "//a[contains(text(),'Launch Series T calculator')]"
    }

    def is_valid(self, url):
        """
        Checks whether `url` is a valid URL.
        """
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def verify_title(self):
        title = self.driver.title
        print(title)
        assert title

    def verify_header(self):
        header = self.driver.find_element_by_xpath(self.locators["header_text"]).text
        assert header

    def verify_active_breadcrumb(self):
        breadcrumb = self.driver.find_element_by_xpath(self.locators["active_breadcrumb"]).text
        assert breadcrumb

    def verify_illustration_tool_opens(self):
        self.driver.find_element_by_xpath(self.locators["launch_illustration_tool"]).click()
        time.sleep(1)
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        print(self.driver.title)
        assert "Sun Life Global Investments".casefold() in (self.driver.title).casefold()

    def verify_granite_tool_opens(self):
        self.driver.find_element_by_xpath(self.locators["launch_granite_tool"]).click()
        time.sleep(1)
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        print(self.driver.title)
        assert "Sun Life Granite Managed Solutions Proposal Tool".casefold() in (self.driver.title).casefold()

    def verify_series_t_cal_tool_opens(self):
        self.driver.find_element_by_xpath(self.locators["launch_series_t_calculator"]).click()
        time.sleep(1)
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
        print(self.driver.title)
        assert "Sun Life Series T Calculator".casefold() in (self.driver.title).casefold()
