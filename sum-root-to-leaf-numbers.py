# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0 
        return sum([int(x) for x in self.roottoLeaf(root)])
    
    def roottoLeaf(self, root):
        # root is not None
        # return a list of string form of all numbers from root to leaf
        if not root.left and not root.right:
            return [str(root.val)]
        elif not root.left:
            return [str(root.val) + x for x in self.roottoLeaf(root.right)]
        elif not root.right:
            return [str(root.val) + x for x in self.roottoLeaf(root.left)]
        else:
            return [str(root.val) + x for x in self.roottoLeaf(root.left) + self.roottoLeaf(root.right)]
