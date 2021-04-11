from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/')

time.sleep(1)

# link_reset_password = driver.find_element_by_link_text('Forgot your password?')
# link_reset_password.click()

link_reset_password = driver.find_element_by_partial_link_text('Forgot')
link_reset_password.click()

time.sleep(5)

driver.close()