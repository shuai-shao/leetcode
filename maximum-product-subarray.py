################################################################################################
# O(n^2) solution
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if not A:
            return None
        max_prod = A[0]
        for i in range(1,len(A)):
            new_prod = 1
            count = 0 
            while count <= i:
                new_prod = new_prod*A[i-count]
                if new_prod > max_prod:
                    max_prod = new_prod
                count = count + 1
        return max_prod
################################################################################################
# O(n) solution 
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if not A:
            return None
        max_pre = A[0]
        min_pre = A[0]
        global_max = A[0]
        for i in range(1, len(A)):
            max_cur = max(max_pre*A[i], min_pre*A[i], A[i])
            min_cur = min(max_pre*A[i], min_pre*A[i], A[i])
            global_max = max(global_max, max_cur)
            max_pre = max_cur
            min_pre = min_cur 
        return global_max
