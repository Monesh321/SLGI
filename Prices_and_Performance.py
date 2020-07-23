import time
from urllib.parse import urljoin
from selenium import webdriver
import requests
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



baseurl = "https://www.sunlifeglobalinvestments.com/"


class Prices_and_performance():
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "Daily_prices_fund_names": "//table[@id='TABLE_1']//tr//a",
        "Daily_prices_fund_data": "//table[@id='TABLE_1']//td",
        "Fund_input_box": "//input[@id='fund']",
        "Asset_class_dropdown": "//select[@id='asset-class']",
        "Series_dropdown": "//select[@id='series']",
        "Currency_dropdown": "//select[@id='currency']",
        "Show_funds_button": "//input[@name='show-funds']",
        "table1": "TABLE_1",
        "table2": "TABLE_2",
        "table3": "TABLE_3",
        "table4": "TABLE_4",
        "table5": "TABLE_5",

    }
    def verify_title(self):
        title=self.driver.title
        print(title)
        assert title

    def get_all_data_from_a_table(self, table_id):
        
        table = self.driver.find_element(By.ID, table_id)
        rows = table.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        for row in rows:
            # Get the columns (all the column 2)
            cols = [col.text for col in row.find_elements(By.TAG_NAME, "td")]  # note: index start from 0, 1 is col 2
            if cols != []:
                print(cols)  # prints text from the element

    def show_funds(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.locators["Fund_input_box"]).send_keys("Sun Life Granite Balanced Class")
        select_asset = Select(self.driver.find_element_by_xpath(self.locators["Asset_class_dropdown"]))
        # select by visible text
        time.sleep(2)
        select_asset.select_by_visible_text('Portfolio Solutions')

        select_series = Select(self.driver.find_element_by_xpath(self.locators["Series_dropdown"]))
        time.sleep(1)
        select_series.select_by_visible_text('A')
        select_currency = Select(self.driver.find_element_by_xpath(self.locators["Currency_dropdown"]))
        time.sleep(1)
        select_currency.select_by_visible_text('CAD')
        self.driver.find_element_by_xpath(self.locators["Show_funds_button"]).click()
        time.sleep(1)
        self.get_all_data_from_a_table(self.locators["table1"])

    def verify_funds(self):
        alllinks = self.driver.find_elements_by_xpath(self.locators["Daily_prices_fund_names"])
        linktexts = [link.text for link in alllinks]
        linkurls = [urljoin(baseurl, link.get_attribute("data-link")) for link in alllinks]
        print(len(linktexts))
        for url in linkurls:
            print(url)

    def verify_fund_data(self):
        alldata = self.driver.find_elements_by_xpath(self.locators["Daily_prices_fund_data"])
        print([data.text for data in alldata])
