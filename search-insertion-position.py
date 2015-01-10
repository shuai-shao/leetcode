class Solution:
    # A is a sorted array of numbers
    # if target value found, return the index, else return the insertion position
    # use [1,3,5,6] as an example
    def searchInsert(self, A, target):
        if not A : 
            return 0
        if target < A[0]:
            return 0
        if target > A[-1]:
            return len(A)
        low = 0 
        high = len(A) - 1
        while low < high:
            mid = low + (high - low) / 2
            if A[mid] >= target:
                high = mid
            else:
                low = mid + 1
        return high
