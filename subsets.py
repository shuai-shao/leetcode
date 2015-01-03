class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if not S:
            return [[]]
        else:
            S.sort()
            pre_subsets = self.subsets(S[1:])
            return pre_subsets + [[S[0]]+elem for elem in pre_subsets]
