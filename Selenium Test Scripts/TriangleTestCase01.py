# The intent of this test case is to use a single variable to create an equilateral triangle

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html")
driver.implicitly_wait(10)

sideLength = 5

driver.find_element(By.NAME, "side1").send_keys(sideLength)
driver.find_element(By.NAME, "side2").send_keys(sideLength)
driver.find_element(By.NAME, "side3").send_keys(sideLength)

driver.find_element(By.ID, "identify-triangle-action").click()

driver.quit()