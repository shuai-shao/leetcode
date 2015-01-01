class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        previous = 1
        current = 1
        if n == 1 or n == 0:
            return 1
        else:
            for i in range(1,n):
                previous, current = current, previous + current
            return current
            
            //dynamic programming
