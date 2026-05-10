from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")

print(driver.title)

input("Press Enter to close browser...")

driver.quit()