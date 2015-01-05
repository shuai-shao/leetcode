# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        level = []
        result = []
        queue = []
        
        if root:
            queue.append(root)
            queue.append(None)    # None indicates the end of each level 
        
        while queue:
            node = queue.pop(0)
            if node:    # not the end of a level
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:    # end of a level
                result.insert(0,level)    # the only difference from the twin problem
                level = []
                if queue:
                    queue.append(None)
                    
        return result      
                
