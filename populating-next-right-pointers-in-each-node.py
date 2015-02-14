# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        queue = []
        if root:
            queue.append(root)
            queue.append(None)
        while queue:
            current = queue.pop(0)
            if current:
                current.next = queue[0]
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            else:
                if queue:
                    queue.append(None)
