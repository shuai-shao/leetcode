class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return '1'
        else:
            s_new = ''
            s_old = self.countAndSay(n-1)
            length = len(s_old)
            if length == 1:
                return '1' + s_old
            else:
                i = 0
                while i < length:
                    count = 1
                    while i < length-1 and s_old[i+1] == s_old[i]:
                        i += 1
                        count += 1
                    s_new = s_new + str(count) + s_old[i]
                    i += 1
                return s_new
