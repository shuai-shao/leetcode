#####################################################################################
# O(n) solution 
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        for i in range(len(num)-1):
            if num[i+1]<num[i]:
                return num[i+1]
        return num[0]
#####################################################################################
# O(logn) solution binary search
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        lo = 0
        hi = len(num) - 1
        while lo < hi:
            mid = lo + (hi-lo)/2
            if num[mid] < num[hi]:
                hi = mid
            else:
                lo = mid + 1
        return num[lo]
