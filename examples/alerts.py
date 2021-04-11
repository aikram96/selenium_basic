from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver.maximize_window()

driver.get('http://testautomationpractice.blogspot.com')

time.sleep(3)

alert_btn = driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button')
alert_btn.click()

alert_obj = driver.switch_to.alert

#Retrieve the message on the Alert window
msg = alert_obj.text
print ("Alert shows following message: "+ msg )

time.sleep(2)

# use the accept() method to accept the alert
# alert_obj.accept()
# print("--- Clicked on the OK Button in the Alert Window ---")

#use the dismiss() method to accept the alert
alert_obj.dismiss()
print("--- Clicked on the CANCEL Button in the Alert Window ---")

time.sleep(2)

# Menu dropdowns

speed_dropdown = Select(driver.find_element_by_id('speed'))
speed_dropdown.select_by_visible_text('Medium')

file_dropdown = Select(driver.find_element_by_id('files'))
file_dropdown.select_by_value('2')

number_dropdown = Select(driver.find_element_by_id('number'))
number_dropdown.select_by_visible_text('4')

product_dropdown = Select(driver.find_element_by_id('products'))
product_dropdown.select_by_value('Microsoft')

animal_dropdown = Select(driver.find_element_by_id('animals'))
animal_dropdown.select_by_value('big baby cat')

time.sleep(2)

driver.close()
