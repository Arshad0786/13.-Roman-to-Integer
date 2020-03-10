import unittest
from RomanToInteger import Solution


class TwoSumTest(unittest.TestCase):
    def test_last_two(self):
        temp = Solution()
        self.input = "III"
        self.assertEqual(temp.romanToInt("III"), 3)
        


if __name__ == "__main__":
    unittest.main()
