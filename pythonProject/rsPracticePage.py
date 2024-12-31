import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
actions = ActionChains(driver)
driver.maximize_window()
time.sleep(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
expectedUrl = "https://rahulshettyacademy.com/AutomationPractice/"
currentUrl = driver.current_url
assert expectedUrl in currentUrl
print(currentUrl, "matches with", expectedUrl)
time.sleep(2)
radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
print("No. of radio buttons:", len(radioButtons))
i = 0
for radioButton in radioButtons:
    radioButtons[i].click()
    time.sleep(1)
    i += 1
    time.sleep(1)
print("Clicked on radio buttons")
time.sleep(1)
selectCountry = driver.find_element(By.CSS_SELECTOR, 'input[id="autocomplete"]')
selectCountry.send_keys('India')
time.sleep(1)
selectIndia = driver.find_element(By.CSS_SELECTOR, 'li.ui-menu-item:nth-child(2)')
India = selectIndia.text
time.sleep(1)
selectIndia.click()
selectedCountry = "India"
time.sleep(1)
assert selectedCountry in India
print("The country selected from dropdown is:", India)
time.sleep(1)
ddOptions = driver.find_element(By.CSS_SELECTOR, "#dropdown-class-example")
noOfDds = driver.find_elements(By.CSS_SELECTOR, "#dropdown-class-example")
print("No. of dropdowns:", len(noOfDds))
noOfOptions = ddOptions.find_elements(By.CSS_SELECTOR, "option")
print("No. of options in the dropdown:", len(noOfOptions))
time.sleep(1)
indexes = [0, 1, 2, 3, 0]
for index in indexes:
    Select(ddOptions).select_by_index(index)
    time.sleep(1)
options = ["Select", "Option1", "Option2", "Option3"]
print(options)
for index, option in enumerate(options):
    Select(ddOptions).select_by_visible_text(option)
    assert option in ddOptions.text
    print(index+1, option)
    time.sleep(1)
time.sleep(4)
