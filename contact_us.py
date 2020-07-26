from urllib.parse import urlparse

import requests

# from requests_html import HTML
homeurl = "https://www.sunlifeglobalinvestments.com/Slgi"


class contact_us():
    def __init__(self, driver):
        self.driver = driver

    q1_text = """Canada Post

                SLGI Asset Management Inc.,
                30 Adelaide Street East, Suite 1
                Toronto, Ontario  M5C 3G9

                Courier

                SLGI Asset Management Inc.,
                30 Adelaide Street East, Suite 1
                Toronto, Ontario  M5C 3G9""".strip().splitlines()

    q1_text = [i.strip() for i in q1_text if i != ""]

    q2_text = """Sign in or register to our advisor site, or contact our wealth sales team at 1-877-837-7844""".strip().splitlines()

    q2_text = [i.strip() for i in q2_text if i != ""]

    q3_text = """Step 1: If you have a problem or concern about a specific transaction, contact your financial advisor or one of our client service representatives.

    Phone: 1-877-344-1434
    
    Fax: 1-855-329-7544
    
    Email: info@sunlifeglobalinvestments.com
    
    Mail:
    
    SLGI Asset Management Inc.,
    1 York Street,
    Toronto,ON M5J 0B6
    
    Step 2: If your concern is not resolved to your satisfaction, contact the Manager, Client Services for SLGI Asset Management Inc. using the contact methods above.
    
    Step 3: To request additional consideration, you may refer your concern to our Sun Life Financial Ombudsman.
    
    Mail:
    
    Ombudsman's Office
    Sun Life Financial
    1 York Street,
    Toronto,
    ON M5J 0B6
    
    Email:ombudsman@sunlife.com
    
    Fax: 416-595-1431 or 514-866-2548
    
    Step 4: If you wish to pursue your concern after following the steps above, contact the Ombudsman for Banking Services and Investments (OBSI).
    
    The OBSI, as part of a national industry-based dispute resolution system for consumers of financial services, deals with concerns about banking and securities investment products and services that have not been resolved through the company's dispute resolution system.
    
    Phone: 1-888-451-4519 or 1-416-287-2877""".strip().splitlines()

    q3_text = [i.strip() for i in q3_text if i != ""]

    def is_valid(self, url):
        """
              Checks whether `url` is a valid URL.
        """
        parsed = urlparse(url)
        status = requests.get(url).status_code
        if bool(parsed.netloc) and bool(parsed.scheme) and status == 200:
            return True
        else:
            print("STATUS:", status)
            print("DOMAIN:", parsed.netloc, "SCHEME:", parsed.scheme)
            return False

    locators = {
        "title_header": "//div[@class='title-bar']//h1[contains(text(),'Contact us')]",
        "breadcrumb_text": "//ol[@class='breadcrumb']//li[@class='active']//span[contains(text(),'Contact us')]",
        "phone": "//p[contains(text(),'Phone: 1-877-344-1434')]",
        "fax": "//p[contains(text(),'Fax: 1-855-329-7544')]",
        "email": "//p[contains(text(),'Email:')]/a",
        "Q1": "//div[@class='accordion-head']//a[contains(text(),'Where can I mail mutual fund applications and form')]",
        "q1_body": "//div[@id='collapse1']//p",
        "Q2": "//div[@class='accordion-head']//a[contains(text(),'Are you a mutual fund licensed advisor?')]",
        "q2_body": "//div[@id='collapse2']//p",
        "Q3": "//div[@class='accordion-head']//a[contains(text(),'Concerns or complaints')]",
        "q3_body": "//div[@id='collapse3']//p"
    }

    def verify_title(self):
        title = self.driver.title
        print(title)
        assert title

    def verify_header_present(self):
        header = self.driver.find_element_by_xpath(self.locators["title_header"]).text
        assert "Contact us".casefold() in header.casefold()

    def verify_breadcrumb_active(self):
        breadcrumb = self.driver.find_element_by_xpath(self.locators["breadcrumb_text"]).text
        assert breadcrumb

    def verify_phone_displayed(self):
        phone = self.driver.find_element_by_xpath(self.locators["phone"]).text
        assert phone

    def verify_fax_displayed(self):
        fax = self.driver.find_element_by_xpath(self.locators["fax"]).text
        assert fax

    def verify_email_displayed(self):
        email = self.driver.find_element_by_xpath(self.locators["email"]).text
        assert "info@sunlifeglobalinvestments.com".casefold() in email.casefold()

    def verify_Question_1(self):
        Q1 = self.driver.find_element_by_xpath(self.locators["Q1"]).click()
        body1 = self.driver.find_elements_by_xpath(self.locators["q1_body"])
        # for actual, expected in itertools.zip_longest(body1, self.q1_text):
        #     print("EXPECTED TEXT_LINE:", expected)
        #     print("ACTUAL TEXT_LINE:", (actual.text).strip())
        #     assert expected in actual.text
        for i in body1:
            print(i.text)

    def verify_Question_2(self):
        Q2 = self.driver.find_element_by_xpath(self.locators["Q2"]).click()
        body2 = self.driver.find_elements_by_xpath(self.locators["q2_body"])
        # for actual, expected in itertools.zip_longest(body2, self.q2_text):
        #     print("EXPECTED TEXT_LINE:", expected)
        #     print("ACTUAL TEXT_LINE:", actual.text)
        #     assert expected in actual.text
        for i in body2:
            print(i.text)

    def verify_Question_3(self):
        Q3 = self.driver.find_element_by_xpath(self.locators["Q3"]).click()
        body3 = self.driver.find_elements_by_xpath(self.locators["q3_body"])
        # for actual, expected in itertools.zip_longest(body3, self.q3_text):
        #     print("EXPECTED TEXT_LINE:", expected)
        #     print("ACTUAL TEXT_LINE:", actual.text)
        #     assert expected in actual.text
        for i in body3:
            print(i.text)

