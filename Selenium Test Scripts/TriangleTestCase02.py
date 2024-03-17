from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html")
driver.implicitly_wait(10)

text = driver.find_element(By.XPATH, '/html/body/div/h1')
print(text)

driver.quit()