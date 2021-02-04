import unittest

class Operations(unittest.TestCase):

    def test_sum(self):
        sum = 1 + 1
        self.assertEqual(sum, 2, msg="Sum result was valid")

    def test_rest(self):
        rest = 1 - 1
        self.assertNotEqual(rest, 2)

    def test_isupper(self):
        self.assertTrue("COURSE".isupper())
        self.assertFalse("course".isupper())

if __name__ == '__main__':
    unittest.main()
