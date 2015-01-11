##########################################################################################
# O(n) solution similar tp but simpler than product counterpart 
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A:
            return None
        allmax = A[0]
        premax = A[0]
        for i in range(1, len(A)):
            cur = max(premax+A[i],A[i])
            allmax = max(allmax,cur)
            premax = cur 
        return allmax
  
##########################################################################################
