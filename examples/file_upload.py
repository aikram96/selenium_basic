from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.maximize_window()

driver.get("http://testautomationpractice.blogspot.com/")


driver.switch_to.frame("frame-one1434677811")

file_upload_btn = driver.find_element_by_id("RESULT_FileUpload-10")
time.sleep(10)
file_upload_btn.send_keys("C:\\Users\\aikra\\Desktop\\paisaje.jpg")

time.sleep(3)

message = driver.find_elements_by_class_name('form_table')
print("Upload message: ", message[0].text)

time.sleep(2)

driver.quit()