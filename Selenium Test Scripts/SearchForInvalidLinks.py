# This test case opens my older portfolio website and checks all links in the homepage to see if the links work or not.

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Firefox, website and maximise the window
driver1 = webdriver.Firefox()
driver1.implicitly_wait(10)
driver1.get("https://sigrothian.co.uk/")
driver1.maximize_window()

# Collect all href links, searches all links to see if the status code is above 400 and returns valid or broken
allLinks = driver1.find_elements(By.TAG_NAME, 'a')
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

# Close Firefox
driver1.quit()

# Repeat the test case in Google Chrome
driver2 = webdriver.Chrome()
driver2.implicitly_wait(10)
driver2.get("https://sigrothian.co.uk/")
driver2.maximize_window()

allLinks = driver2.find_elements(By.TAG_NAME, 'a')
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

driver2.quit()