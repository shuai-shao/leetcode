class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            return 1.0/self.pow(x,-n)
        if n == 0:
            return 1.0
        temp = self.pow(x,n/2)
        if n % 2 == 0:
            return temp*temp
        else:
            return temp*temp*x
            
            
# the point of this problem is using divide and conquer algorithm to obtain O(logn) solution 
# trick here is to store the temp 
