from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver.maximize_window()

driver.get('file:///C:/Users/aikra/Downloads/table.html')

time.sleep(1)

# Verify the number of elements
rows = len(driver.find_elements_by_xpath('/html/body/table/tbody/tr'))
cols = len(driver.find_elements_by_xpath('/html/body/table/tbody/tr[2]/td'))
title = len(driver.find_elements_by_xpath('/html/body/table/tbody/tr[1]/th'))

print("Number of elements in every row: ", rows)
print("Number of elements in every col: ", cols)
print("Number of elements in the title: ", title)

# Iterations for the title
for t in range(1, title+1):
    title_value = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/th['+str(t)+']')
    title_val_txt = title_value.text
    print(title_val_txt, end='          ')
print()

# Iterations for the table: rows and cols
for r in range(2, rows+1):
    for c in range(1, cols+1):
        value = driver.find_element_by_xpath('/html/body/table/tbody/tr['+str(r)+']/td['+str(c)+']')
        val_txt = value.text
        print(val_txt, end='          ')
    print()

time.sleep(5)

driver.close()
