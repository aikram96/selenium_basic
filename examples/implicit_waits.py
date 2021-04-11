from selenium import webdriver
import unittest

class implicit_waits(unittest.TestCase):

    def setUp(self):
        # pre conditions
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        # implicitly wait is not efficiently cause you have to set a specific time
        self.driver.implicitly_wait(time_to_wait=10)

    def test_login_page(self):
        # first test
        tittle_login_page = self.driver.title
        self.assertEqual(tittle_login_page, "OrangeHRM")


    def test_valdiate_login(self):
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
    unittest.main()
