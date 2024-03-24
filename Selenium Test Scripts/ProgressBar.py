
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://demoqa.com/progress-bar")
driver.maximize_window()

button = driver.find_element(By.ID, "startStopButton")
button.click()
time.sleep(5)
button.click()

driver.quit()