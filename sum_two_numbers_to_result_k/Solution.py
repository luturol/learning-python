class Solution(object):
    def two_sum(self, list, k):
        values = set()
        for i in range(len(list)):
            if list[i] == k:
                return True
            elif k - list[i] in values:
                return True
            else:
                values.add(list[i])
        
        return False

print(Solution().two_sum([4, 7, 1, -3, 2], 5))