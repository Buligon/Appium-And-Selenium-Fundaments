""" 
* check if:
* 1. none 'delete' element comes within the page
* 2. add element works
* 3. delete element works
* 4. multiple add element works (to 10)
* 5. multiple delete element works (to 10)
todo: verify if its UI is working properly
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/Firefox.exe"
driver = webdriver.Firefox(options=options)



def get_delete_elements():
  delete_element[:] = driver.find_elements(By.CLASS_NAME, 'added-manually')

try:
  wait = WebDriverWait(driver, 10)
  driver.get('https://the-internet.herokuapp.com')

  add_remove_elements_link = wait.until(EC.presence_of_element_located(
    (By.LINK_TEXT, 'Add/Remove Elements')
  ))

  add_remove_elements_link.click()

  add_element = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, 'button[onclick="addElement()"]')
  ))
  
  add_element.click()

  delete_element = list()

  get_delete_elements()

  assert len(delete_element) == 1

  delete_element[0].click()

  get_delete_elements()

  assert len(delete_element) == 0

  i = 0
  while i < 10:
    add_element.click()
    i+=1

  get_delete_elements()

  assert len(delete_element) == 10

  for element in delete_element:
    element.click()

  get_delete_elements()
  
  assert len(delete_element) == 0

finally:
  driver.quit()