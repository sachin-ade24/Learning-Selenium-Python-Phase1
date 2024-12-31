import time

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

expectedUrl = "https://www.facebook.com/"
phoneNo = "9420653966"
password_ = 'M@toshri2000'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.get(expectedUrl)
time.sleep(5)
emailAddrOrPhoneNo = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Email address or phone number"]')
emailAddrOrPhoneNo.send_keys(phoneNo)
time.sleep(2)
password = driver.find_element(By.CSS_SELECTOR, '[aria-label="Password"]')
password.send_keys(password_)
time.sleep(2)
loginBtn = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="royal_login_button"]')
loginBtnText = loginBtn.text
loginBtn.click()
time.sleep(10)

