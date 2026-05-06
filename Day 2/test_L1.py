import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):
    def test_sum(self):
        calc = Calculator(8,2)
        self.assertEqual(calc.get_sum(), 10, "The answer was not 10.")

    # Test for the remaining operations...
    def test_div(self):
        calc = Calculator(8,2)
        self.assertEqual(calc.get_div(), 4, "The answer was wrong.")

    def test_diff(self):
        calc = Calculator(8,2)
        self.assertEqual(calc.get_diff(), 6, "The answer was wrong.")
    
    def test_prod(self):
        calc = Calculator(8,2)
        self.assertEqual(calc.get_prod(), 16, "The answer was wrong.")

if __name__ == "__main__":
    unittest.main()