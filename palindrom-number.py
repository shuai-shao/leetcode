# since no extra space is allowed, you can't convert the number into string first, as that requires
# extra space. It's also not idea to reverse the whole number, as that might overflow. We can come up
# with an idea that is not language-dependent and more generic. 
# The idea here is to compare the first and last digit of the number, and so on so forth.
class Solution:
    # given a number num, return a boolean indicating whether num is a palindrome
    def isPalindrome(self,num):
        if num < 0:  # negative number is defined to be non-palindrome here
            return False 
        #if num == 0:
        #    return True
        # first, find the proper divisor to obtain the first digit of the num
        div = 1
        while num/div >= 10:
            div = div*10
        while num > 0:
            first = num / div
            last = num % 10
            if first != last:
                return False
            num = (num % div) / 10    # pop both the first and the last digits
            div = div/100
        return True  
