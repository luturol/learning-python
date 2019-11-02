class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.value)
            output += " "
            node = node.next
        
        return output
    
    # Iterative Solution
    def reverseIteratively(self, head):
        tail = head.next
        while tail.next != None:
            tail = tail.next            
        tailHead = tail
        node = head
        while node.next != None:
            if node.next.value == tail.value:
                tail.next = ListNode(node.value)
                tail = tail.next
                node.next = None
                node = head
            else:
                node = node.next

        head = tailHead

    # Recursive Solution
    def reverseRecursively(self, head):
        tail = self.getTail(head)
        self.reverseRecursively0(head, tail)
    

    def getTail(self, head):
        if head.next != None:
            return self.getTail(head.next)
        else:
            return head

    def reverseRecursively0(self, head, tail):
        if head.next != None and head.next.value == tail.value:
            tail.next = ListNode(head.value)
            tail = tail.next
            head.next = None
            self.reverseRecursively0(self, tail)
        elif head.next == None:
            head = tail
        else:
            self.reverseRecursively0(head.next, tail)

    def will_answer(self, head):
        if(head.next == None):
            return head
        else:
            next = self.will_answer(head.next)
            next.next = head
            return head

# Test program
# Initialize the test list
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial List:")
print(testHead.printList())


def will_answer(head):
    if(head.next == None):
        return head
    else:
        next = will_answer(head.next)
        next.next = head
        return head

# reversal
testHead.will_answer(testHead)
#testHead.reverseRecursively(testHead)
#respotaWill = will_answer(testHead)
testHead.next = None
print(testTail.printList())
