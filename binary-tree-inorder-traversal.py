########################################################################################################
# inorder: left-node-right
# recursive solution
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)    
        
########################################################################################################
# iterative
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        result = []
        current = root
        while current.left != None:
            current = current.left
            stack.append(current)
        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.right:
                current = current.right
                stack.append(current)
                while current.left != None:
                    current = current.left
                    stack.append(current)
                
        return result
########################################################################################################  
# http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/   nice article about inorder traversal 
# if no extra memrory is allowed, Morris Traversal is a good algorithm: http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
