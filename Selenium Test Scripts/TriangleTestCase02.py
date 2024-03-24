# The intent of this test case is to see if the webdriver can read the static text.
# Due to minimal ways to identify the static text element and likely not enough knowledge, this test case fails due
# to being unable to convert the element into the text that is displayed on the front end

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html")
driver.implicitly_wait(10)

text = driver.find_element(By.TAG_NAME, "p")
assert text == "Enter the lengths of the three sides of a triangle. The program will inform you if the triangle is equilateral, isosceles or scalene."

driver.quit()