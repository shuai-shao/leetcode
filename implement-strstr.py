# brute force solution, O(mn), where m is the length of needle and n is the length of haystack.
class Solution:
    def strStr(self, haystack, needle):
        m = len(needle)
        n = len(haystack)
        if m == 0:
            return 0 
        #if n == 0:
        #    return -1
        #if m > n :
        #    return -1 
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1
                
