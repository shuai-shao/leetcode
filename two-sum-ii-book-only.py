# solution one is using binary search, time complexity O(nlogn), space complexity O(1)
# we can do better! solution two is by using two pointers, O(n) time complexity, O(1) space complexity

class Solution:
    # num: a list of sorted integers
    # target: target number
    # return (index1, index2)
    # e.g. num = [1,2,4,5,6,8], target = 11
    def twoSum(self, num, target):
        i = 0 
        j = len(num) - 1
        while i < j:
            if num[i] + num[j] < target:
                i = i + 1
            elif num[i] + num[j] > target:
                j = j - 1
            else:
                return (i+1, j+1)
        return (None, None)
