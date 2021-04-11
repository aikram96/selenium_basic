from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="../drivers/geckodriver.exe")

driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/')
time.sleep(5)

driver.quit()