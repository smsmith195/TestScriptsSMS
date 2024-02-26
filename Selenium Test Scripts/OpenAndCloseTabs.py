import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# location of firefox driver
s = webdriver.FirefoxService()
firefoxOptions = Options()
firefoxOptions.headless = False

# Open Browser and website
driver = webdriver.Firefox(service=s, options=firefoxOptions)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Search for 'Cheesecake' in the search field
driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("cheesecake")
driver.find_element(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input").click()

time.sleep(4)

# Capture the search results and print the number of search results, this should be 5
searchResults = driver.find_elements(By.XPATH, "//*[@id='wikipedia-search-result-link']")
print(len(searchResults))

# Print the link text of all Wikipedia search results and click on all five links to open them in new tabs
for link in searchResults:
    link.find_element(By.TAG_NAME, "a").click()

# Capture the unique IDs of all tabs
windowIDs = driver.window_handles

time.sleep(4)

# Switch to all tabs and print the tab titles
for winID in windowIDs:
    driver.switch_to.window(winID)
    print(driver.title)

# Close all tabs at once
driver.quit()
