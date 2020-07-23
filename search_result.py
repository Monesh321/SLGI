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


# from requests_html import HTML
homeurl = "https://www.sunlifeglobalinvestments.com/Slgi/Search+results?q=investment&action=input"


class search_result():
    def __init__(self, driver):
        self.driver = driver

    locators = {
        "search_header": "//h1[contains(text(),'Search results')]",
        "breadcrumb_text":"//ol[@class='breadcrumb']//li[@class='active']//text()",
        "result_count": "//span[@id='search-result-num-results']",
        "result_links": "//div[@id='search-result-items']//a",
        "pagination": "//ul[@id='search-result-pagination']//li",
        "previous_enabled":"//li[@class='previous']"
    }

    def verify_header_present(self):
        pass