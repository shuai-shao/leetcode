class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        else:
            present = head
            next_nd = head.next
            while next_nd != None:
                if next_nd.val == present.val:
                    present.next = next_nd.next
                    next_nd = next_nd.next
                else:
                    present = next_nd
                    next_nd = present.next
            return head
