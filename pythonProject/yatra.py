
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
print(driver.title)
time.sleep(2)
# checkBox1 = driver.find_element(By.XPATH, "(//i[@class='ico ico-checkbox'])[2]")
checkBox2 = driver.find_element(By.XPATH, "(//a[@class='custom-check'])[3]")
checkBox2.click()
time.sleep(2)
print(checkBox2.is_selected())

if driver.find_element(By.XPATH, "(//a[@class='custom-check'])[3]").is_selected()==False:
   print('test case failed')

driver.find_element(By.XPATH, "//i[@class='ico ico-checkbox ico-checkbox-checked']").is_selected()
print(driver.find_element(By.XPATH, "(//a[@class='custom-check'])[3]").is_selected())
print(driver.find_element(By.XPATH, "//i[@class='ico ico-checkbox ico-checkbox-checked']").is_selected())



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# # Specify the path to your web driver executable
# # driver_path = "C://My Folder/Selenium/chromedriver-win64/chromedriver-win64/chromedriver.exe"
# # Update with the path to your driver
#
# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome("C://My Folder/Selenium/chromedriver-win64/chromedriver-win64/chromedriver.exe")
#
# # Navigate to a website
# driver.get("https://www.example.com")
# time.sleep(10)



# # Find an element by its CSS selector (replace with the appropriate selector for your webpage)
# element = driver.find_element("css selector", "#some-element")
#
# # Perform an action (e.g., typing text into an input field)
# element.send_keys("Hello, Selenium!")
#
# # Wait for a few seconds (optional)
# time.sleep(2)
#
# # Perform another action (e.g., pressing Enter)
# element.send_keys(Keys.RETURN)
#
# # Wait for a few seconds (optional)
# time.sleep(2)
#
# # Close the browser window
# driver.quit()

