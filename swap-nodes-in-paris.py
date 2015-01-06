#################################################################################################
# recursive solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        A = head
        B = head.next
        B.next = self.swapPairs(B.next)
        A.next = B.next
        B.next = A
        
        return B
        
#################################################################################################
# iterative solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        start = ListNode(0)    # create a new node 
        start.next = head
        
        cur = start
        while cur.next != None and cur.next.next != None:
            cur.next = self.swap(cur.next, cur.next.next)
            cur = cur.next.next
            
        return start.next
        
    def swap(self, next1, next2):
        next1.next = next2.next
        next2.next = next1
        return next2
