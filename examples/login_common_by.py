from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/')

time.sleep(1)
username = driver.find_element(By.NAME, 'txtUsername')
password = driver.find_element(By.ID, 'txtPassword')
# Put values
username.send_keys('Admin')
password.send_keys('admin123')

time.sleep(1)
login_btn = driver.find_element(By.XPATH, '//*[@id="btnLogin"]')
# Click on screen
login_btn.click()
time.sleep(2)

welcome_btn = driver.find_element(By.PARTIAL_LINK_TEXT, 'Welcome')
welcome_btn.click()
time.sleep(2)
logout_btn = driver.find_element(By.LINK_TEXT, 'Logout')
logout_btn.click()

time.sleep(5)

driver.close()