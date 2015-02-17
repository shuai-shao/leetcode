# use dictionary to map value to its index
# O(n) time, O(n) space

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in range(len(num)):
            if target - num[i] not in dict:
                dict[num[i]] = i+1
            else:
                return (dict[target-num[i]],i+1)
