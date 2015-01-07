class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
        return [self._binarytoInt(s) for s in self._gray(n)]
        
    def _gray(self,n):   # helper function, return a list of binary code
        if n == 1:
            return ['0','1']
        return ['0' + x for x in self._gray(n-1)] + [ '1' + x for x in self._gray(n-1)[::-1]]
    
    def _binarytoInt(self,s):    # given a string representing binary numbers, return an integer
        result = 0
        for i in s:
            result = result*2
            result = result + int(i) 
        return result
