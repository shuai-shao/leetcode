############################################################################################################
#very elegent iterative solution. seems vague at the first glance. drawing a graph will help you understand
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        cur = root
        while cur:
            if cur.left:
                pre = cur.left 
                while pre.right:
                    pre = pre.right
                cur.right, cur.left, pre.right = cur.left, None, cur.right
            cur = cur.right
      
############################################################################################################                
# recursive solution 
# the only kinda tricky part is return the tail of the flattened tree
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.flatTail(root)
        
    def flatTail(self, root):    # helper function, flattern the tree and return the last element
        cur = root
        while cur and (cur.left or cur.right):
            if cur.left:
                tail = self.flatTail(cur.left)
                cur.right, cur.left, tail.right, cur = cur.left, None, cur.right, tail
            else:
                cur = cur.right
        return cur 
                    
                
