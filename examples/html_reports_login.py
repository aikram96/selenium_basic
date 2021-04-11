from selenium import webdriver
import unittest
import HtmlTestRunner

class unittest_login(unittest.TestCase):

    def setUp(self):
        # pre conditions
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()

    def test_login_page(self):
        # first test
        tittle_login_page = self.driver.title
        self.assertEqual(tittle_login_page, "OrangeHRM")

    def test_validate_login(self):
        # second test
        username = self.driver.find_element_by_id('txtUsername')
        password = self.driver.find_element_by_id('txtPassword')
        username.send_keys("Admin")
        password.send_keys("admin123")
        login_btn = self.driver.find_element_by_id('btnLogin')
        login_btn.click()

        main_menu = self.driver.find_element_by_id("mainMenu")
        self.assertTrue(main_menu.is_displayed(), msg="It was impossible to login")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../reports', report_name='Login unittest'))