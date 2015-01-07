# about how roman numerals work: http://www.onlineconversion.com/roman_numerals_advanced.htm
# and this http://baike.baidu.com/link?url=KPtlECZIsaJDNzjQ5kKFaVyCY4vpIU5qxAuXrUncrWd_ctDi1q4H3HFMEkVpAU8Q
# the idea is, if a roman numeral is smaller than its previous numeral, add it to the result. otherwise, subtract twice
# the previous numeral and add the present numeral
class Solution:
    # @return an integer
    def romanToInt(self, s):
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        pre = 10000
        rst = 0 
        for i in s:
            cur = dic[i]
            if cur > pre:
                rst = rst - pre - pre + cur
            else:
                rst = rst + cur
            pre = cur
        return rst
