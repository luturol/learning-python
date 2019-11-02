class Solution(object):
    def getRange(self, arr, target):
        indexFirst = -1
        indexLast = -1

        for i, element in enumerate(arr):
            if target == element and indexFirst == -1:
                indexFirst = i
            elif target == element:
                indexLast = i
        if indexLast == -1:
            indexFirst = -1

        return [indexFirst, indexLast]

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 8
print(Solution().getRange(arr, x))