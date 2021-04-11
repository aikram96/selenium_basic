from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.maximize_window()
#Set URL
driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(4)

link_orange = driver.find_element_by_partial_link_text("Orange")
link_orange.click()

print(driver.current_window_handle)

handles = driver.window_handles # return whole handle values of the open windows' web

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "OrangeHRM":
        driver.close()

driver.quit()