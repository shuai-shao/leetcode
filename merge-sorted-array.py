class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if n > 0:
            if m == 0:
                for j in range(n):
                    A.insert(j,B[j])    // it seems append or extend or copy can’t pass the annoying [] and [1] test
            else:
                i = 0
                j = 0
                len_a = m
               
                while i < len_a and j < n:
                    if A[i] > B[j]:
                        A.insert(i,B[j])
                        j = j + 1
                        len_a += 1
                    i = i + 1
               
                while j < n:
                    A.insert(m+j,B[j]) // same here, append or extend can’t pass test, not sure why 
                    j = j + 1
                   
