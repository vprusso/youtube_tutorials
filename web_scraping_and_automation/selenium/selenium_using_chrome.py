# YouTube Video: https://www.youtube.com/watch?v=eDrFWRi13DY
from selenium import webdriver

# Old way of doing things that works with Firefox
# driver = webdriver.Firefox()
# driver.get("http:google.com")

chromedriver = "/home/captainhampton/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("http:google.com")
