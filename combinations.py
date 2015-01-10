class Solution:
    # return a list of lists of integers
    # C(n)(k) = C(n-1)(k-1) + C(n-1)(k)
    def combine(self, n, k):
        if n == 0 or k > n or k <= 0:
            return [[]]
        if n == 1:
            return [[1]]
        if k == n :
            return [[x for x in range(1,n+1)]]
        list1 = self.combine(n-1,k)
        list2 = self.combine(n-1,k-1)
        return [x+[n] for x in list2] + list1
            
