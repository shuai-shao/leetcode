class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        if not S:
            return [[]]
        else:
            S.sort()
            pre_subsets = self.subsetsWithDup(S[1:])
            return pre_subsets + [[S[0]]+elem for elem in pre_subsets if [S[0]]+elem not in pre_subsets]
