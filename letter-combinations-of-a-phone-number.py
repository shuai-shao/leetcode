class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if digits == '':
            return ['']
        else:
            result = []
            dic = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
            for letter in dic[digits[0]]:
                result.extend([letter + prev for prev in self.letterCombinations(digits[1:])])   # recursive solution
            return result
            
