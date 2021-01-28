from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver.maximize_window()

driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')

time.sleep(1)



time.sleep(2)

driver.close()