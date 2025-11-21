"""
Unit tests for safe_division function

This test suite validates that the safe_division function correctly handles
various scenarios including normal division, negative numbers, edge cases,
and most importantly, division by zero.
"""

import unittest
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """Test cases for safe_division function"""
    
    def test_normal_division(self):
        """Test normal positive number division"""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(100, 4), 25.0)
        self.assertEqual(safe_division(7, 2), 3.5)
    
    def test_negative_numbers(self):
        """Test division with negative numbers"""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_division_by_zero(self):
        """Test that division by zero returns None instead of raising error"""
        self.assertIsNone(safe_division(10, 0))
        self.assertIsNone(safe_division(-10, 0))
        self.assertIsNone(safe_division(0, 0))
    
    def test_zero_dividend(self):
        """Test division where dividend is zero (but divisor is not)"""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(0, -5), 0.0)
    
    def test_floating_point_numbers(self):
        """Test division with floating point numbers"""
        self.assertAlmostEqual(safe_division(10.5, 2.5), 4.2)
        self.assertAlmostEqual(safe_division(7.5, 1.5), 5.0)
    
    def test_large_numbers(self):
        """Test division with large numbers"""
        self.assertEqual(safe_division(1000000, 1000), 1000.0)
        self.assertEqual(safe_division(999999, 3), 333333.0)
    
    def test_small_numbers(self):
        """Test division with very small numbers"""
        self.assertAlmostEqual(safe_division(0.001, 0.1), 0.01)
        self.assertAlmostEqual(safe_division(1, 1000), 0.001)
    
    def test_result_type(self):
        """Test that result is always float (or None for division by zero)"""
        result = safe_division(10, 2)
        self.assertIsInstance(result, float)
        result = safe_division(10, 0)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
