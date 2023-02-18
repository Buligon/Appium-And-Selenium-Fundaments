from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/Firefox.exe"
driver = webdriver.Firefox(options=options)

try:
  driver.get('https://the-internet.herokuapp.com')
  driver.find_element(By.LINK_TEXT, 'Form Authentication')

  els = driver.find_elements(By.TAG_NAME, 'a')
  print(f'There were {len(els)} anchor elements')

  els = driver.find_elements(By.TAG_NAME, 'foo')
  print(f'There were {len(els)} foo elements')

finally:
  driver.quit()