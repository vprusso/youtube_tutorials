'''
	Here's how you go about authenticating yourself! The important thing to
	note here is that this script will be used in the other examples so
	set up a test user with API credentials and set them up in auth.ini.
'''

from imgurpython import ImgurClient
from helpers import get_input, get_config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def authenticate():
	# Get client ID and secret from auth.ini
	config = get_config()
	config.read('auth.ini')

	client_id = config.get('credentials', 'client_id')
	client_secret = config.get('credentials', 'client_secret')

	imgur_username = config.get('credentials', 'imgur_username')
	imgur_password = config.get('credentials', 'imgur_password')

	client = ImgurClient(client_id, client_secret)

	# Authorization flow, pin example (see docs for other auth types)
	authorization_url = client.get_auth_url('pin')
	
	driver = webdriver.Firefox()
	driver.get(authorization_url)

	# Extract lists of "buyers" and "prices" based on xpath. 
	username = driver.find_element_by_xpath('//*[@id="username"]')
	password = driver.find_element_by_xpath('//*[@id="password"]')
	username.clear()
	username.send_keys(imgur_username)
	password.send_keys(imgur_password)

	driver.find_element_by_name("allow").click()

	timeout = 5
	try:
		element_present = EC.presence_of_element_located((By.ID, 'pin'))
		WebDriverWait(driver, timeout).until(element_present)
		pin_element = driver.find_element_by_id('pin')
		pin = pin_element.get_attribute("value")
	except TimeoutException:
		print("Timed out waiting for page to load")
	driver.close()

	# ... redirect user to `authorization_url`, obtain pin (or code or token) ...
	credentials = client.authorize(pin, 'pin')
	client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
	print("Authentication successful! Here are the details:")

	return client

# If you want to run this as a standalone script, so be it!
if __name__ == "__main__":
	authenticate()