from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver.maximize_window()

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

time.sleep(1)

# Select n source and target

drop_content = driver.find_element_by_id('dropContent')
source_elements = driver.find_elements_by_class_name('dragableBox')
print("------- Capitals: -------")
for x in range(1, 14):
    if x%2 !=0:
        print(source_elements[x].text)


country_content = driver.find_element_by_id('countries')
target_elements = driver.find_elements_by_class_name('dragableBoxRight')
print("------- Countries: -------")
for i in range(0, 7):
    print(target_elements[i].text)

print("------- Finish -------")

time.sleep(1)

# Select 1 source and target
source_element = driver.find_element_by_id('box3')
target_element = driver.find_element_by_id('box103')

action_chains = ActionChains(driver)
action_chains.drag_and_drop(source=source_element, target=target_element).perform()
print("------- Successfully test -------")
time.sleep(2)

driver.close()