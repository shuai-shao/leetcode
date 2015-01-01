# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head == None or head.next == None:
            return None
        else:
            length = 1
            present = head
            while present.next != None:
                length += 1
                present = present.next
           
            target = length - n
            if target == 0:
                head = head.next
            else:
                present = head
                for i in range(target-1):
                    present = present.next
                present.next = present.next.next
        return head
