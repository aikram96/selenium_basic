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

pim_btn = driver.find_element_by_id('menu_pim_viewPimModule')
pim_btn.click()

time.sleep(1)
pim_config_btn = driver.find_element_by_id('menu_pim_Configuration')
pim_config_btn.click()
time.sleep(1)
optional_btn = driver.find_element_by_id('menu_pim_configurePim')
optional_btn.click()
time.sleep(1)
deprecated_checkbox = driver.find_element_by_id('configPim_chkDeprecateFields')
print("Is it select? " + str(deprecated_checkbox.is_selected()))
print("Is it enable? " + str(deprecated_checkbox.is_enabled()))
print("Is it on the screen? " + str(deprecated_checkbox.is_displayed()))

time.sleep(1)

edit_btn = driver.find_element_by_id('btnSave')
edit_btn.click()

time.sleep(5)

driver.close()