import unittest

from expenses_helper import get_timestamp


class Get_Timestamp_Test(unittest.TestCase):
    def test_something(self):
        self.assertEqual(get_timestamp(2022, 10, 10), 1665356400.0)
    def test_something2(self):
        self.assertEqual(get_timestamp(2022, 4, 4), 1649026800.0)




if __name__ == '__main__':
    unittest.main()
