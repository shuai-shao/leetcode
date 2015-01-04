class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        lista = list(a)
        listb = list(b)
        result = ''
        extra = 0
        
        while lista or listb:
            if lista:
                numa = int(lista.pop())
            else:
                numa = 0
            if listb :
                numb = int(listb.pop())
            else:
                numb = 0
            sum = numa + numb + extra
            extra = sum//2
            sum = sum % 2
            result = str(sum) + result
        if extra == 1:
            result = str(extra) + result
            
        return result
            
            
