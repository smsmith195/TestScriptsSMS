# This script demonstrates refreshing a page, navigating backwards and forwards, and clicking a few buttons

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
"""

Code has been commented out due to using a website that has since been updated.
Update using updated web links and so on will be made in the future.

# Open Browser and website
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://sigrothian.co.uk/")
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//div[@class='container']//div[@class='navigation-trigger']").click()
driver.find_element(By.LINK_TEXT, "Contact").click()

driver.find_element(By.NAME, "your-name").send_keys("John Doe")
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)

driver.find_element(By.NAME, "your-name").send_keys("John Doe")
driver.find_element(By.NAME, "your-email").send_keys("dragonking820@yahoo.co.uk")
driver.find_element(By.NAME, "your-subject").send_keys("Automated Test")
driver.find_element(By.NAME, "your-message").send_keys(
    "Have you heard of the critically acclaimed MMORPG Final Fantasy XIV?"
    "With an expanded free trial which you can play through the entirety of A Realm Reborn, Heavensward,"
    "AND the nomination-winning Stormblood expansion up to level 70 for free with no restrictions on playtime"
)
driver.find_element(By.CSS_SELECTOR, "input[value='Send']").click()

driver.quit()
"""