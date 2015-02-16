# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        root_val = postorder.pop()
        root = TreeNode(root_val)
        for i in xrange(len(inorder)): # xrange, not range
            if inorder[i] == root_val:
                root.right = self.buildTree(inorder[i+1:],postorder)   # this part is tricky, can't switch the order of right and left
                root.left = self.buildTree(inorder[:i],postorder)
                break
        return root
