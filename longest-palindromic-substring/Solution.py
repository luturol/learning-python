class Solution(object):
    def longestPalindrome(self, s):
        set = []
        for i in range(len(s)):
            word = s[i]
            for j in range(i, len(s)):
                j += 1
                if j + 1 <= len(s):
                    word += s[j]
                    set.append(word)
               
        longestLength = 0
        longestWord = ""
        for word in set:
            reversed = word[::-1]
            if word == reversed and len(word) > longestLength:
                longestWord = word
                longestLength = len(word)

        return longestWord
                
