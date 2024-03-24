# The intent of this test case is to use a two different valued variables to create a valid triangle

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html")
driver.implicitly_wait(10)

sideLengthA = 5
sideLengthB = 8

driver.find_element(By.NAME, "side1").send_keys(sideLengthA)
driver.find_element(By.NAME, "side2").send_keys(sideLengthB)
driver.find_element(By.NAME, "side3").send_keys(sideLengthA)

driver.find_element(By.ID, "identify-triangle-action").click()

driver.quit()