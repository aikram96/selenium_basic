from ddt import ddt, data, file_data
from selenium import webdriver
import unittest

@ddt
class DataDrivenLogin(unittest.TestCase):

    def setUp(self):
        # pre conditions
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()

    # @data("admin", 3, -3)
    @file_data("../config/data_login.json")
    def test_validate_login(self, value_username, value_password):

        username = self.driver.find_element_by_id('txtUsername')
        password = self.driver.find_element_by_id('txtPassword')
        username.send_keys(value_username)
        password.send_keys(value_password)
        login_btn = self.driver.find_element_by_id('btnLogin')
        login_btn.click()

        main_menu = self.driver.find_element_by_id("mainMenu")
        self.assertTrue(main_menu.is_displayed(), msg="It was impossible to login")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()