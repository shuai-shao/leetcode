class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        rst = [[]]
        for x in num:
            rst = [r[:i] + [x] + r[i:] for r in rst for i in range(len(r)+1)]
        return rst
