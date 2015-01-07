# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        queue = []
        level = []
        result = []
        queue.append(root)
        queue.append(None)
        while queue:
            node = queue.pop(0)
            if node:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                result.append(level)
                level = []
                if queue:
                    queue.append(None)
        for i in range(1,len(result),2):
                result[i] = result[i][::-1]
            
        return result       
