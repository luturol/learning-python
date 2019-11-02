import unittest
from Solution import Solution

class TestLengthOfLongestSubstring(unittest.TestCase):
    def test_shouldReturn10(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abrkaabcdefghijjxxx"), 10, "Should return 10")

    def test_shouldReturn6(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("rafael"), 6, "Should return 6")

    def test_shouldReturn3(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("yellow"), 3, "Should return 3")

if __name__ == "__main__":
    unittest.main()