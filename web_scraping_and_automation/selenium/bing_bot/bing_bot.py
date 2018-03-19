from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import csv
import os
import random
import time


class BingBot(object):
    """Automatically login to Bing and search random words
    to accumulate rewards."""
    def __init__(self, email, password, is_mobile=False):

        self.login_url = "https://login.live.com/"
        self.bing_url = "https://www.bing.com/"

        self.word_list = "word_list.txt"

        self.email = email
        self.password = password

        self.is_mobile = is_mobile

        self.explicit_wait = 3
        self.min_search_wait = 2
        self.max_search_wait = 5
        self.num_searches_to_perform = 10

        self.profile = self.firefox_profile()
        self.driver = webdriver.Firefox(self.profile)

    def firefox_profile(self):
        """Searching on mobile in additon to desktop yields
        more daily points."""
        profile = webdriver.FirefoxProfile()
        if self.is_mobile:
            profile.set_preference("general.useragent.override", "Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0")
        return profile

    def login(self):
        """Automatically login to Bing account."""
        self.driver.get(self.login_url)

        email_input = self.driver.find_element_by_name("loginfmt")
        email_input.send_keys(self.email)

        self.driver.find_element_by_id("idSIButton9").click()

        wait = WebDriverWait(self.driver, self.explicit_wait)
        wait.until(EC.presence_of_all_elements_located((By.ID, "idSIButton9")))

        password_input = self.driver.find_element_by_name("passwd")
        password_input.send_keys(self.password)

        wait = WebDriverWait(self.driver, self.explicit_wait)
        wait.until(EC.presence_of_all_elements_located((By.ID, "idTd_PWD_KMSI_Cb")))

        self.driver.find_element_by_id("idSIButton9").click()

    def get_rand_search_time(self):
        """To be a bit less consistent, randomize time for next search."""
        return random.uniform(self.min_search_wait, self.max_search_wait)

    def get_rand_search_term(self):
        """Randomly select search term for Bing from word list."""
        total_bytes = os.stat(self.word_list).st_size
        random_point = random.randint(0, total_bytes)
        file = open(self.word_list)
        file.seek(random_point)
        file.readline()
        return file.readline()

    def bing_search(self):
        """Navigate to Bing and perform random searches."""
        self.driver.get(self.bing_url)

        wait = WebDriverWait(self.driver, self.explicit_wait)
        wait.until(EC.presence_of_all_elements_located((By.ID, "sb_form_q")))

        for search in range(self.num_searches_to_perform):
            rand_time = self.get_rand_search_time()
            time.sleep(rand_time)

            rand_word = self.get_rand_search_term()
            self.driver.get("http://bing.com/search?q="+rand_word)

    def quit(self):
        """Close the browser."""
        self.driver.close()

    def run(self):
        """Run the primary login, search, quit protocol."""
        self.login()
        self.bing_search()
        self.quit()


with open('bing_accounts.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        user_id = row[0]
        password = row[1]

        bing_bot = BingBot(user_id, password, is_mobile=True)
        bing_bot.run()
        
        bing_bot = BingBot(user_id, password)
        bing_bot.run()

