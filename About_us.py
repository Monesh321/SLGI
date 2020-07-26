import time
from urllib.parse import urlparse

homeurl = "https://www.sunlifeglobalinvestments.com/"


class About_us():
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "header_text": "//div[@class='banner-content left']//h1[contains(text(),'About us')]",
        "active_breadcrumb": "//ol[@class='breadcrumb']//li[@class='active']//span[contains(text(),'About us')]",
        "who_we_are": "//a[contains(text(),'Learn about who we are')]",
        "sub_advisors": "//a[contains(text(),'Read about our sub-advisors')]",
        "sponsorships": "//a[contains(text(),'Learn about sponsorships')]"
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

    def move_to_who_we_are_page(self):
        self.driver.find_element_by_xpath(self.locators["who_we_are"]).click()
        time.sleep(2)
        print(self.driver.title)
        assert "who we are".casefold() in (self.driver.title).casefold()

    def move_to_Investment_management_page(self):
        self.driver.find_element_by_xpath(self.locators["sub_advisors"]).click()
        time.sleep(2)
        print(self.driver.title)
        assert "Investment management".casefold() in (self.driver.title).casefold()

    def move_to_sponsorship_page(self):
        self.driver.find_element_by_xpath(self.locators["sponsorships"]).click()
        time.sleep(1)
        print(self.driver.title)
        assert "Sponsorships".casefold() in (self.driver.title).casefold()
