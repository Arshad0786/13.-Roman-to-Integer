import unittest
from RomanToInteger_recurrence import Solution


class TwoSumTest(unittest.TestCase):
    def test_add(self):
        temp = Solution()
        self.input = "MDCLXVI"
        self.assertEqual(temp.romanToInt(self.input), 1666)

    def test_subtract(self):
        temp = Solution()
        self.input = "XLIV"
        self.assertEqual(temp.romanToInt(self.input), 44)



if __name__ == "__main__":
    unittest.main()
