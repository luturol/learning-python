import unittest
from Solution import Solution

class TestValidateBalancedParentheses(unittest.TestCase):
    def test_Should_Return_True(self):
        self.assertTrue(Solution().isValid("[{()}]"))

    def test_Should_Return_True_Giving_Correct_Pairs(self):
        self.assertTrue(Solution().isValid("[]{}()"))

    def test_Should_Return_False_Giving_Missing_Brackets(self):
        self.assertFalse(Solution().isValid("[{()}"))

    def test_Should_Return_False_Giving_Missing_Brace(self):
        self.assertFalse(Solution().isValid("[()}]"))

    def test_Should_Return_False_Giving_Missing_Parentheses(self):
        self.assertFalse(Solution().isValid("[{(}]"))
    
    def test_Should_Return_False_Giving_Missing_Braces_And_Parantheses(self):
        self.assertFalse(Solution().isValid("}("))
    
    def test_Should_Return_False_Giving_Wrong_Order_Braces(self):
        self.assertFalse(Solution().isValid("}{"))

if __name__ == "__main__":
    unittest.main()