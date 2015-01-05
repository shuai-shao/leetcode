# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        level = []
        queue = []
        if root:
            queue.append(root)
            queue.append(None)    # None indicates the end of each level
        
        while queue:
            node = queue.pop(0)
            if node:    # node is not None
                level.append(node.val)
                if node.left:   # left subtree exists
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:    # node is None, end of the level 
                result.append(level)   # append the whole level to result
                level = []
                if queue:
                    queue.append(None)
                    
        return result
                
                
 # level order traversal, or breadth-first-search (bfs)
                
                
                        
            
                
