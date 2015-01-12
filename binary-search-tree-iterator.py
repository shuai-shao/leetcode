# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# The idea here is using a stack to store next minimum number 

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.stack = []
        cur = self.root
        while cur:
            self.stack.append(cur)
            cur = cur.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.stack:
            return True
        else:
            return False

    # @return an integer, the next smallest number
    def next(self):
        nextSmall = self.stack.pop()
        x = nextSmall.right
        while x:
            self.stack.append(x)
            x = x.left
        return nextSmall.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
