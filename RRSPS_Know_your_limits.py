import time
from urllib.parse import urlparse

homeurl = "https://www.sunlifeglobalinvestments.com/"


class RRSPS():
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "header_text": "//div[@class='title-bar-brighter-lnp']//h1[contains(text(),'Investor education')]",
        "article_header": "//div[@class='article-header']//h2[contains(text(),'RRSPs: Know your limits')]",
        "active_breadcrumb": "//ol[@class='breadcrumb']//a[contains(text(),'Investor education')]",
        "advisor_tools_n_cal": "//div[@class='col-xs-12 col-sm-6 col-md-12 col-lg-12 right-rail-module col-height']//a[contains(text(),'Advisor tools and calculators')]"
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

    def verify_article_header(self):
        header = self.driver.find_element_by_xpath(self.locators["article_header"]).text
        assert header

    def verify_active_breadcrumb(self):
        breadcrumb = self.driver.find_element_by_xpath(self.locators["active_breadcrumb"]).text
        assert breadcrumb

    def verify_advisor_tools_and_calculators(self):
        tnc = self.driver.find_element_by_xpath(self.locators["advisor_tools_n_cal"])
        tnc.click()
        time.sleep(4)
        title=self.driver.title
        print(title)
        time.sleep(1)
        assert "Advisor tools and calculators".casefold() in title.casefold()


