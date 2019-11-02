import unittest
from Solution import Solution

class TestLongestPalindromicSubstring(unittest.TestCase):
    def test_Should_Return_Anana(self):
        self.assertEqual(Solution().longestPalindrome('banana'), 'anana')

    def test_Should_Return_Arara(self):
        self.assertEqual(Solution().longestPalindrome('arara'), 'arara')
        
if __name__ == "__main__":
    unittest.main()