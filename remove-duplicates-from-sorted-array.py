class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        else:
            i = 0
            j = 0
            while i < len(A)-1:
                if A[i+1] == A[i]:
                    i = i + 1
                else:
                    j = j + 1
                    A[j] = A[i+1]
                    i = i + 1
            A = A[:j+1]
            return j+1
           
       
