# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        cur = head
        n = 0 
        while cur:
            n = n + 1
            cur = cur.next
        cur = head
        parent, cur = self._buttomUp(cur, 0, n-1)    # remember to pass back cur to do the increment cur=cur.next
        return parent
        
    def _buttomUp(self, cur, start, end):
        if start > end:
            return None, cur
        if start == end:
            parent = TreeNode(cur.val)
            cur = cur.next
            return parent, cur
        mid = (start + end) / 2
        left,cur = self._buttomUp(cur, start, mid-1)
        parent = TreeNode(cur.val)
        parent.left = left
        cur = cur.next
        right,cur = self._buttomUp(cur, mid + 1, end)
        parent.right = right 
        return parent, cur
