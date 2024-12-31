import time

from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
time.sleep(2)
driver.get('https://rahulshettyacademy.com/angularpractice/')
time.sleep(2)
actions = ActionChains(driver)
# driver.find_element(By.CSS_SELECTOR, "[class*='form-control']").send_keys('Sachin')
userName = driver.find_element(By.CSS_SELECTOR, "[class*='form-control']" and "input[name='name']")
userName.send_keys('Sachin Ade')
time.sleep(1)
emailId = driver.find_element(By.CSS_SELECTOR, "[class*='form-control']" and "input[name='email']")
emailId.send_keys('Sachin@xyz.com')
time.sleep(1)
password = driver.find_element(By.CSS_SELECTOR, '[id="exampleInputPassword1"]')
password.send_keys('abc12345')
time.sleep(1)
checkBox = driver.find_element(By.CSS_SELECTOR, '[id="exampleCheck1"]')
actions.move_to_element(checkBox).click().perform()
time.sleep(1)
selectDd = driver.find_element(By.CSS_SELECTOR, 'select[id="exampleFormControlSelect1"]')
Select(selectDd).select_by_visible_text('Female')
time.sleep(1)
employedRb = driver.find_element(By.CSS_SELECTOR, '[id="inlineRadio1"]')
actions.move_to_element(employedRb).click().perform()
time.sleep(5)

