# This test case hovers over a menu element and then moves on to hovering over a sub-menu

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://demoqa.com/menu")
driver.maximize_window()

menu_element = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/a')
hover = ActionChains(driver).move_to_element(menu_element)
hover.perform()

menu_element2 = driver.find_element(By.XPATH, '//*[@id="nav"]/li[2]/ul/li[3]/a')
hover = ActionChains(driver).move_to_element(menu_element2)
hover.perform()

driver.quit()
