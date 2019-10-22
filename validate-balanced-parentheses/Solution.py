class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == "{" or s[i] == "[" or s[i] == "(":
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                value = stack.pop()
                brackets = (value == "[" and s[i] == "]")
                parentheses = (value == "(" and s[i] == ")")
                braces = (value == "{" and s[i] == "}")
                if not brackets and not parentheses and not braces:
                    return False 
        if len(stack) == 0:
            return True