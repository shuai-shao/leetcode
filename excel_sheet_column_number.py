class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        if len(s) == 0:
            return 0
        else:
            return ord(s[len(s)-1]) - ord('A') + 1 + 26 * self.titleToNumber(s[:len(s)-1])
           
