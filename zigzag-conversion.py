class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        dic = {}
        result = []
        for i in range(nRows):
            dic[i] = []
        delta = -1
        i, j = 0, 0
        while j < len(s):
            dic[i].append(s[j])
            if i == 0 or i == nRows-1:
                delta = delta*(-1)
            i = i + delta
            j = j + 1
        for i in range(nRows):
            result.extend(dic[i])
        return ''.join(result)
