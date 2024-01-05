from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Initialize the Chrome WebDriver
s = Service('D:\Selenium\selenium-python\selenium-python-main\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Open Google
driver.get("http://www.google.com")

# Find the search box element and enter a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("NPRU")

search_box.send_keys(Keys.RETURN)

# Wait for the search results to load (ideally, use WebDriverWait instead of time.sleep)
time.sleep(5)

# Print the title of the current page
print(driver.title)

# Close the browser
driver.quit()
