from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/Firefox.exe"
# open the session and get things ready with IDs and all
driver = webdriver.Firefox(options=options)
try:
  driver.get('https://the-internet.herokuapp.com')
finally:
  # delete the session
  driver.quit()