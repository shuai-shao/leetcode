###############################################################################################################
# recursive solution 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        else:
            return self.isMirror(root.left, root.right)
            
    def isMirror(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        elif left.val != right.val:
            return False
        else:
            return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

################################################################################################################
# iterative solution 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        level = []
        queue = []
        
        if root:
            queue.append(root)
            queue.append(None)
            
            while queue:
                node = queue.pop(0)
                if node != None and node != '#':
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    else:
                        queue.append('#')     # position holder
                    if node.right:
                        queue.append(node.right)
                    else:
                        queue.append('#')
                elif node == '#':
                    level.append(node)
                else:   # end of a level
                    if level != level[::-1]:    # check if a level is symmetric
                        return False
                    level = []
                    if queue:
                        queue.append(None)
                
        return True
