# basic_selenium
Basic training to know how to use selenium python with chrome and firefox driver

Selenium - Chrome - Python

1. python install
search stable version to download: 3.7 or more
>> https://www.python.org/downloads/

2. Verify if the installation were correct:

2.A Open CMD and put
>> python -version
Should be read the version of your python

2.B Open GIT BASH and put
>> python --version
Should be read the version of your python

3. Pycharm install
>> https://www.jetbrains.com/es-es/pycharm/
Follow the manual instructions

>> Open the pycharm
>> Create a new directory, you can called: "Automatización"

4. Select the language PYTHON for Selenium Web driver 
>> https://www.selenium.dev/downloads/
Selenium Client & Web Driver for the language.

>> Open the Pycharm' terminal (down side)
>> Put: pip install selenium

5. Choose the CONTROLLER
Browsers for the web navegator.
Chrome could be your option

>> Click on DOCUMENTATION
>> Depends of your operative system, you select the best option
If you use WINDOWNS --> Should be select: chromedriver -win32
>> Decompress the zip file downloaded in any directory
>> Copy the .exe "chromedriver.exe" (Right click and copy)
>> Right click and copy into the directory created on Pycharm --> "Automatización"
>> Select New Python Pakcage and called "drivers"
>> Right click on the new directory "drivers"  page and accept
Should be see: chromerdriver.exec 

>> Right click on the directory "Automatización" and select New directory called "Examples"
>> Right click on the directory "Examples" and select New Python File called "FirstScripts"
If you review the extention of the file created should be finishes in .py
>> Copy and page the follow code:

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver.maximize_window()

driver.get('https://opensource-demo.orangehrmlive.com/')
time.sleep(5)

driver.quit()

>> This script can help you tu start open different pages automated like youtube, emails, whatever you need to open (: 
