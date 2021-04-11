from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/')

time.sleep(1)
username = driver.find_element_by_id('txtUsername')
password = driver.find_element_by_id('txtPassword')
# Put values
username.send_keys('Admin')
password.send_keys('admin123')

time.sleep(1)
login_btn = driver.find_element_by_id('btnLogin')
# Click on screen
login_btn.click()
time.sleep(5)

driver.close()