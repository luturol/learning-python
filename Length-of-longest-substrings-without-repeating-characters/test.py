import unittest

from solution import Solution

class TestLengthOfLongestSubstringWithoutRepeatingCharacter(unittest.TestCase):
    
    def test_should_return_10(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abrkaabcdefghijjxxx"), 10, "Should return 10")

    
    def test_should_return_6(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("rafael"), 6, "Should return 6")
    
    def test_should_return_4(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("william"), 4, "Should return 4")

if __name__ == "__main__":
    unittest.main()