import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Browser and website
driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://demo.opencart.com/")
driver.maximize_window()

# Dead link search
allLinks = driver.find_elements(By.TAG_NAME, 'a')
count = 0

for link in allLinks:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, " is a broken link")
        count += 1
    else:
        print(url, " is a valid link")

print("Total number of broken links: ", count)

driver.quit()