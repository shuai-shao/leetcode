# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        for i in xrange(len(inorder)):
            if inorder[i] == root_val:
                root.left = self.buildTree(preorder, inorder[:i])   # same trick here, see inorder and postorder 
                root.right = self.buildTree(preorder, inorder[i+1:])
                break
        return root
