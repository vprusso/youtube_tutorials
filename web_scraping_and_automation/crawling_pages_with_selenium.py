from selenium import webdriver

# # Open up a Firefox browser and navigate to web page. 
# driver = webdriver.Firefox()
# driver.get("http://econpy.pythonanywhere.com/ex/001.html")

# # Extract lists of "buyers" and "prices" based on xpath. 
# buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
# prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

# # Print out all of the buyers and prices on page:
# num_page_items = len(buyers)
# for i in range(num_page_items):
# 	print(buyers[i].text + " : " + prices[i].text)

# # Clean up (close browser once completed task). 
# driver.close()

# ------
MAX_PAGE_NUM = 5
MAX_PAGE_DIG = 3
driver = webdriver.Firefox()
for i in range(1, MAX_PAGE_NUM + 1):
	page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i) 
	url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"
	
	driver.get(url)

	buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
	prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

	num_page_items = len(buyers)
	for i in range(num_page_items):
		print(buyers[i].text + " : " + prices[i].text)

driver.close()