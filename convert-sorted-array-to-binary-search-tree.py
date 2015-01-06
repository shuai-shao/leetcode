# divide the array from middle point
# if both left and right subtrees are legit height balanced BST, you can prove that the whole tree is legit HBBST.
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        mid = num[len(num)/2]
        new_node = TreeNode(mid)
        new_node.left = self.sortedArrayToBST(num[:len(num)/2])
        new_node.right = self.sortedArrayToBST(num[len(num)/2+1:])
        return new_node
