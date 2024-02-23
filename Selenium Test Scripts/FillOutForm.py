# This test case will fill in information into a test website form

# 1 - Open web browser of choice
# 2 - Fill in a name in the 'Name' field
# 3 - Fill in an email address in the 'Email' field
# 4 - Fill in a phone number in the 'Phone' field
# 5 - Fill in a lot of text into the 'Address' field
# 6 - Select an option in the 'Gender' radio button
# 7 - Select multiple day checkboxes in the 'Days' checkbox section
# 8 - Select a country from the 'Country' drop-down menu

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Open Browser and website
driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID, "name").send_keys("John Doe")
driver.find_element(By.ID, "email").send_keys("test@test.com")
driver.find_element(By.ID, "phone").send_keys("1337 343 6969")

driver.find_element(By.ID, "textarea").send_keys(
    "Have you heard of the critically acclaimed MMORPG Final Fantasy XIV?"
    "With an expanded free trial which you can play through the entirety of A Realm Reborn, Heavensward,"
    "AND the nomination-winning Stormblood expansion up to level 70 for free with no restrictions on playtime"
)

radioChoice = driver.find_elements(By.XPATH, "//input[@type='radio']")
for radio in radioChoice:
    choice = radio.get_attribute("value")
    if choice == "female":
        radio.click()

# Checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    selection = checkbox.get_attribute('id')
    if selection == "monday" or selection == "wednesday" or selection == "friday":
        checkbox.click()

# Dropdowns
drpCountry = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
drpCountry.select_by_visible_text("Germany")

driver.quit()