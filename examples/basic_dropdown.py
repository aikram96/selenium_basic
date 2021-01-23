from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

time.sleep(3)

admin_btn = driver.find_element_by_id('menu_admin_viewAdminModule')
admin_btn.click()
time.sleep(2)

user_rol_dropdown = Select(driver.find_element_by_id('searchSystemUser_userType'))
#user_rol_dropdown.select_by_value("2")
#user_rol_dropdown.select_by_index(2)
user_rol_dropdown.select_by_visible_text('ESS')

status_dropdown = Select(driver.find_element_by_id('searchSystemUser_status'))
status_dropdown.select_by_index(1)

search_btn = driver.find_element_by_id('searchBtn')
search_btn.click()

time.sleep(5)

driver.close()