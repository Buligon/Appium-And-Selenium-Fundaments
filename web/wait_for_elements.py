from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/Firefox.exe"
driver = webdriver.Firefox(options=options)

try:
  wait = WebDriverWait(driver, 10)
  driver.get('https://the-internet.herokuapp.com')

  wait.until(EC.presence_of_element_located(
    (By.LINK_TEXT, 'Form Authentication')
  ))

  wait.until(EC.url_to_be('https://the-internet.herokuapp.com/'))


finally:
  driver.quit()