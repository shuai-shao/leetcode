# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None:
            return True
        else:
            if self.height(root.left) - self.height(root.right) in [-1,0,1]:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            else:
                return False
        
    def height(self,root): # calculate the height of a tree with root = root 
        if root == None:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))
''' # the above solution is acceptable, but slow, with complexity O(N^2)
# the trick of the below O(N) solution is the combine height and isbalanced function in one recursion

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        dep, bal = self.dep_and_bal(root)
        return bal
        
    def dep_and_bal(self,root):   # function to return depth and check if balanced at the same time
        if root == None:
            return 0, True
        else:
            ld, lb = self.dep_and_bal(root.left)
            if not lb: 
                return 0, False
            rd, rb = self.dep_and_bal(root.right)
            if not rb:
                return 0, False
            if ld - rd not in [-1,0,1]:
                return 0, False
            else:
                return 1 + max(ld,rd), True
        

