from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import re
import time


class AmazonBot(object):
    """Parses relevant information from a text file consisting of
    Amazon links."""
    def __init__(self, items):
        """Setup bot for Amazon URL."""
        self.amazon_url = "https://www.amazon.ca/"
        self.items = items

        self.profile = webdriver.FirefoxProfile()
        self.options = Options()
        #self.options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_profile=self.profile,
                                        firefox_options=self.options)

        # Navigate to the Amazon URL.
        self.driver.get(self.amazon_url)

        # Obtain the source
        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.html = self.soup.prettify('utf-8')

    def search_items(self):
        """Searches through the list of items obtained from spreadsheet and
        obtains name, price, and URL information for each item."""
        urls = []
        prices = []
        names = []
        for item in self.items:
            print(f"Searching for {item}...")

            self.driver.get(self.amazon_url)
            #select = Select(self.driver.find_element_by_id("searchDropdownDescription"))
            #select.select_by_visible_text('All Departments')

            search_input = self.driver.find_element_by_id("twotabsearchtextbox")
            search_input.send_keys(item)

            time.sleep(2)
            #wait = WebDriverWait(self.driver, self.explicit_wait)
            #wait.until(EC.presence_of_all_elements_located((By.ID, "twotabsearchtextbox")))

            search_button = self.driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
            search_button.click()

            time.sleep(2)

            t = self.driver.find_element_by_id("result_0")
            asin = t.get_attribute("data-asin")
            url = "https://www.amazon.ca/dp/" + asin
            price = self.get_product_price(url)
            name = self.get_product_name(url)
        
            prices.append(price)
            urls.append(url)
            names.append(name)

            print(name)
            print(price)
            print(url)

            time.sleep(2)

        return prices, urls, names

    def get_product_price(self, url):
        """Gets and cleans product price from Amazon page.
        If HTML attribute priceblock_ourprice or priceblock_dealprice
        is absent, the price is marked as Not Available."""
        self.driver.get(url)

        try:
            price = self.driver.find_element_by_id("priceblock_ourprice").text
        except:
            pass

        try:
            price = self.driver.find_element_by_id("priceblock_dealprice").text
        except:
            pass

        if price is None:
            price = "Not available"

        else:
            non_decimal = re.compile(r'[^\d.]+')
            price = non_decimal.sub('', price)

        return price

    def get_product_name(self, url):
        """Returns the product name of the Amazon URL."""
        self.driver.get(url)
        try:
            product_name = self.driver.find_element_by_id("productTitle").text
        except:
            pass

        if product_name is None:
            product_name = "Not available"
        return product_name

    def close_session(self):
        """Close the browser session."""
        self.driver.close()

