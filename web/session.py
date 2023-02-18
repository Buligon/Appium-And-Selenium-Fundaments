from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/Firefox.exe"
# open the session and get things ready with IDs and all
driver = webdriver.Firefox(options=options)

# delete de session
driver.quit()