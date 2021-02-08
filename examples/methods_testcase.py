import unittest

class MethodsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Open Application")


    def setUp(self):
        print("Login on Application")

    def test_create(self):
        print("Test Create")

    def test_update(self):
        print("Test Update")

    def test_search(self):
        print("Test Search")

    def test_delete(self):
        print("Test Delete")

    def tearDown(self):
        print("Logout Application")


    @classmethod
    def tearDownClass(cls):
        print("Close Application")

if __name__ == '__main__':
    unittest.main()
