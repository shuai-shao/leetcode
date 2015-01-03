class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0:
            return 0
        elif x < 0:
            return -1*self.reverse(-x)
        else:
            s = str(x)
            rev_s = s[::-1] 
            i = 0 
            zeros = True
            while i < len(rev_s) and zeros:
                if rev_s[i] == '0':
                    i = i + 1 
                else:
                    zeros = False
            rev_s = rev_s[i:]
            if int(rev_s) > 2147483647:
                return 0 
            else:
                return int(rev_s)
        # I use Python string to do the reverse, one can also use math methods of course. 
