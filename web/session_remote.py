from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/Firefox.exe"

caps = {
  'broserName': 'firefox'
}

driver = webdriver.Remote (
  command_executor = 'http://localhost:4444',
  desired_capabilities = caps,
  options=options
)

driver.quit()