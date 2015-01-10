# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        bool, rst = self.path(root, sum)
        return rst

    def path(self, root, sum):   # return not only the paths, but also if the desired path exists
        if root == None:
            return False, []
        elif not root.left and not root.right:
            if root.val == sum:
                return True, [[root.val]]
            else:
                return False, []
        elif not root.left:
            bool_right, list_right = self.path(root.right, sum - root.val)
            if not bool_right:
                return False, []
            else:
                return True, [[root.val] + x for x in list_right]
        elif not root.right:
            bool_left, list_left = self.path(root.left, sum - root.val)
            if not bool_left:
                return False, []
            else:
                return True, [[root.val] + x for x in list_left]
        else:
            bool_left, list_left = self.path(root.left, sum - root.val)
            bool_right, list_right = self.path(root.right, sum - root.val)
            if bool_left and bool_right:
                return True, [[root.val] + x for x in list_left] + [[root.val] + x for x in list_right]
            elif bool_left:
                return True,[[root.val] + x for x in list_left]
            elif bool_right:
                return True, [[root.val] + x for x in list_right]
            else:
                return False, []
#########################################################################################################
# A neater solution 
# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        bool_total, result = self._pathsum(root, sum)
        return result
        

        
    def _pathsum(self, root, sum):   # helper function that returns whether path exists and a list
        if not root:
            return False, []
        if not root.left and not root.right and root.val == sum:
            return True, [[root.val]]
        bool_left, result_left = self._pathsum(root.left, sum - root.val)
        bool_right, result_right = self._pathsum(root.right, sum - root.val)
        bool_total = bool_left or bool_right
        result = [[root.val] + x for x in result_left if bool_left] + [[root.val] + x for x in result_right if bool_right]
        return bool_total, result
