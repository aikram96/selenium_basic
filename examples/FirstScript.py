from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/')
time.sleep(5)

driver.quit()