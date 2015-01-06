# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root): 
        if not root:
            return True
        result_bool, result_small, result_big = self.valid(root)
        return result_bool
        
        
    def valid(self, root):
        # return valid_bool, smallest number and biggest number
        # root can't be None
        result_bool = True
        result_small = root.val
        result_big = root.val
        if root.left:
            vld, small, big = self.valid(root.left)
            result_bool = result_bool and root.val > big and vld
            result_small = min(result_small,small)
            result_big = max(result_big,big)
        if root.right:
            vld, small, big = self.valid(root.right)
            result_bool = result_bool and root.val < small and vld
            result_small = min(result_small,small)
            result_big = max(result_big,big)
            
        return result_bool, result_small, result_big
            
