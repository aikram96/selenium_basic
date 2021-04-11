from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver.maximize_window()

driver.get('https://www.selenium.dev/selenium/docs/api/java/')

time.sleep(3)

frame_option = driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[2]/ul[1]/li[1]/a')
frame_option.click()

driver.switch_to.frame('packageListFrame')
selenium = driver.find_element_by_xpath('/html/body/main/ul/li[1]/a')
selenium.click()
driver.switch_to.default_content() # change to default content
print('----- First Frame -----')

driver.switch_to.frame('packageFrame')
alert = driver.find_element_by_xpath('/html/body/main/div/section[1]/ul/li[1]/a')
alert.click()
driver.switch_to.default_content() # change to default content
print('----- Second Frame -----')

driver.switch_to.frame('classFrame')
instance_method = driver.find_element_by_xpath('//*[@id="t2"]/span[1]/a')
instance_method.click()
driver.switch_to.default_content() # change to default content
print('----- Third Frame -----')

time.sleep(2)

driver.close()
