# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if k == 0:
            return head
        elif head == None or head.next == None:
            return head
        else:
            present = head
            count = 1
            while present.next != None:    # count length of the list
                present = present.next
                count += 1
                
            present.next = head   # connect the tail and the head of the list
            
            k_eff = k % count    # effective steps of rotation
            
            present = head
            n_move = count - k_eff
            for i in range(n_move-1):    # move to the desired place
                present = present.next
            
            new_head = present.next
            present.next = None
            return new_head
