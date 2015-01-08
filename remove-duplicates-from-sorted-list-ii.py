# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        sentinel = ListNode(0)
        sentinel.next = head
        cur = sentinel
        pioneer = cur.next
        while cur.next:
            count = 1
            while pioneer.next and pioneer.next.val == pioneer.val:
                count = count + 1
                pioneer = pioneer.next
            if count > 1:
                cur.next = pioneer.next
            else:
                cur = cur.next
            pioneer = pioneer.next
                
        return sentinel.next
                
