"""
PURPOSE: Test functions in final project
CSCI 120 - Intro to Computer Science
INSTRUCTOR: Jeff Bush
AUTHOR: Zachery Bingaman
"""

import unittest
import server


class Tester(unittest.TestCase):
    """
    Unit Tester to test functions from server.py
    """

    def test_is_even(self):
        """
        tests the is_even function of server, to ensure that it returns correct boolean values
        """
        self.assertTrue(server.is_even(2))
        self.assertTrue(server.is_even(111111110000))
        self.assertTrue(server.is_even(0))
        self.assertFalse(server.is_even(1))
        self.assertFalse(server.is_even(1111113))


if __name__ == "__main__":
    unittest.main()
