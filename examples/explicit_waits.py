from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import unittest

class explicit_waits(unittest.TestCase):

    def setUp(self):
        # pre conditions
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()


    def test_validate_logout(self):
        # second test
        username = self.driver.find_element_by_id('txtUsername')
        password = self.driver.find_element_by_id('txtPassword')
        username.send_keys("Admin")
        password.send_keys("admin123")
        login_btn = self.driver.find_element_by_id('btnLogin')
        login_btn.click()

        welcome_admin_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Welcome")
        welcome_admin_link.click()

        # time.sleep(2)

        wait = WebDriverWait(self.driver, 10)

        logout_link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        logout_link.click()

        title_login = self.driver.title
        wait.until(ec.title_contains("OrangeHRM"))
        self.assertEqual(title_login, "OrangeHRM")
        print("---- The logout was Successfully ----")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
