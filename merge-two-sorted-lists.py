# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            new_head = ListNode(0)
            present = new_head
            while l1 != None and l2 != None:
                if l1.val <= l2.val:
                    new_node = ListNode(l1.val)
                    present.next = new_node
                    present = present.next
                    l1 = l1.next
                else:
                    new_node = ListNode(l2.val)
                    present.next = new_node
                    present = present.next
                    l2 = l2.next
            if l1 != None:
                present.next = l1
            else:
                present.next = l2
            return new_head.next
    
