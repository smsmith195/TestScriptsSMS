import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("United")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "United States (USA)":
        country.click()
        break

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "United Kingdom (UK)"

driver.quit()