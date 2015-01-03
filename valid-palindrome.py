class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True
        else:
            s = filter(str.isalnum, s.lower())   # str.isalnum() is true for alphanumeric characters
            return s == s[::-1]
            
