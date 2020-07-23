import time
from urllib.parse import urljoin, urlparse

import bs4
from selenium import webdriver
import requests
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from lxml import html


class Signin_form():
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "signin_header": "//h3[contains(text(),'Sign in')]",
        "accessid_input": "//input[@id='USER']",
        "remember_me_checkbox": "//label[contains(text(),'Remember my access ID')]",
        "password": "//input[@id='PASSWORD']",
        "submit_btn": "//input[@class='btn btn-yellow']",
        "forgot_access_id": "//form[@id='form_signon']//a[contains(text(),'Forgot your access ID?')]",
        "forgot_access_password": "//form[@id='form_signon']//a[contains(text(),'Forgot your password?')]",
        "Error": "//div[@class='feature signin']//span[@id='ERROR_HTML']",
        "client_text": "//p[contains(text(),'Call our Client Services team at 1-877-344-1434 to')]",
        "forgot_access_id_page": "//div[@class='pageHeader']",
        "forgot_password_page": "//div[@class='pageHeader']"
    }

    def verify_title(self):
        title = self.driver.title
        print(title)
        assert title

    def verify_signin_header(self):
        header = self.driver.find_element_by_xpath(self.locators["signin_header"])
        print(header.text)
        assert "Sign in".casefold() in (header.text).casefold()

    def verify_signin_functionality(self):
        self.driver.find_element_by_xpath(self.locators["accessid_input"]).send_keys("monesh321")
        self.driver.find_element_by_xpath(self.locators["remember_me_checkbox"]).click()
        self.driver.find_element_by_xpath(self.locators["password"]).send_keys("password")
        time.sleep(3)
        self.driver.find_element_by_xpath(self.locators["submit_btn"]).click()

        title = self.driver.title
        print(title)
        errormsg = self.driver.find_element_by_xpath(self.locators["Error"]).text
        print("ERROR msg: " + errormsg)
        assert errormsg in "The ID and password combination you entered is incorrect. Please try again. Did you forget your Access ID or your password?"

    def client_text_not_present(self):
        text = self.driver.find_element_by_xpath(self.locators["client_text"]).text
        print(text)
        assert "Client".casefold() in text.casefold()

    def verify_forgot_access_ID(self):
        self.driver.find_element_by_xpath(self.locators["forgot_access_id"]).click()
        forgot_text = self.driver.find_element_by_xpath(self.locators["forgot_access_id_page"]).text
        print("NEW TITLE:", self.driver.title)
        print(forgot_text)
        assert "Forgot your Access ID or password?".casefold() in forgot_text.casefold()

    def verify_forgot_password(self):
        self.driver.find_element_by_xpath(self.locators["forgot_access_password"]).click()
        forgot_password_text = self.driver.find_element_by_xpath(self.locators["forgot_password_page"]).text
        print("NEW TITLE:", self.driver.title)
        print(forgot_password_text)
        assert "Password reset" in forgot_password_text
