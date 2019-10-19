class Solution(object):
    def lengthOfLongestSubstring(self,s):
        substrings = []
        substring = ""
        for i in range(len(s)):
            next = i + 1
            if next < len(s) and s[i] != s[next]:
                substring += s[i]
            else:
                substring += s[i]
                substrings.append(substring)
                substring = ""
        
        length = 0
        for i, sub in enumerate(substrings):
            if len(sub) > length:
                length = len(sub)
        
        return length

print(Solution().lengthOfLongestSubstring("abrkaabcdefghijjxxx"))