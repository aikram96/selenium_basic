from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/')

time.sleep(1)
username = driver.find_element_by_css_selector('input[name=txtUsername]')
password = driver.find_element_by_css_selector('input[name=txtPassword]')
# Put values
username.send_keys('Admin')
password.send_keys('admin123')

time.sleep(1)
login_btn = driver.find_element_by_css_selector('input.button')
# Click on screen
login_btn.click()
time.sleep(5)

driver.close()