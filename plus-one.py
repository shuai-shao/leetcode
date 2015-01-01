class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        digits[len(digits)-1] += 1
        stop= False
        i = len(digits) - 1
        while stop == False and i > 0:
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
                i = i - 1
            else:
                stop = True
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0,1)
        return digits
        
