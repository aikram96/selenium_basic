from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/')

time.sleep(1)

link_reset_password = driver.find_element_by_partial_link_text('Forgot')
link_reset_password.click()
time.sleep(1)

reset_username = driver.find_element_by_id('securityAuthentication_userName')
reset_username.send_keys('Admin')

reset_password_btn = driver.find_element_by_class_name('searchValues')
reset_password_btn.click()

time.sleep(5)

driver.close()