import unittest
from assignment import func1

class TestFunc1(unittest.TestCase):
    def test_sum_greater_than_100(self):
        self.assertEqual(func1(60, 50), 110)
    
    def test_sum_equal_to_100(self):
        self.assertEqual(func1(50, 50), 2500)
    
    def test_sum_less_than_100(self):
        self.assertEqual(func1(30, 40), 10)
    
    def test_negative_input(self):
        self.assertEqual(func1(-10, 20), "Error")
        self.assertEqual(func1(10, -20), "Error")
        self.assertEqual(func1(-10, -20), "Error")
    
    def test_zero_input(self):
        self.assertEqual(func1(0, 20), "Error")
        self.assertEqual(func1(20, 0), "Error")
        self.assertEqual(func1(0, 0), "Error")

if __name__ == '__main__':
    unittest.main()
