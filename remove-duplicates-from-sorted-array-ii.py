class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        i = 0 
        j = 0
        while i < len(A):
            count = 1
            while i< len(A)-1 and A[i+1] == A[i]:
                i = i + 1
                count = count + 1
            if count >=2 :
                A[j] = A[i]
                A[j+1] = A[i]
                j = j + 2
            else:
                A[j] = A[i]
                j = j + 1
            i = i + 1
        return j 
           
