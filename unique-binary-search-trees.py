# great notes. check this out: http://cs.lmu.edu/~ray/notes/binarytrees/
# Actually, if you know that number of unique binary search tree is Catalan Number, you can implement using O(1) space 
# Here I use the dynamic programming method, O(n^2) time complexity and O(n) space complexity.
class Solution:
    # @return an integer
    def numTrees(self, n):
        if n == 0 or n == 1:
            return 1
        num = [0 for i in range(n+1)]
        num[0] = 1
        num[1] = 1
        for i in range(2,n+1):
            if i % 2 == 0:
                i_range = i/2
                for j in range(i_range):
                    num[i] += num[j]*num[i-1-j]
                num[i] = num[i]*2
            else:
                i_range = (i-1)/2
                for j in range(i_range):
                    num[i] += num[j]*num[i-1-j]
                num[i] = num[i]*2 
                num[i] += num[i_range]*num[i_range]
        return num[n]
                
