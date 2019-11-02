class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution(object):
    def addTwoNumbers(self, list1, list2):
        converted1 = self.getConvertedValue(list1)
        converted2 = self.getConvertedValue(list2)
        
        sum = converted1 + converted2
        sumList = None
        for digit in str(sum)[::-1]:
            if sumList is None:
                sumList = ListNode(digit)
            else:
                node = sumList
                while node.next is not None:
                    node = node.next
                node.next = ListNode(digit)
        
        return sumList

    def getConvertedValue(self, list):
        value = ""
        while list:
            value += str(list.value)
            list = list.next
        
        return int(value[::-1])

list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)

list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)

result = Solution().addTwoNumbers(list1,list2)
while result:
    print(result.value)
    result = result.next