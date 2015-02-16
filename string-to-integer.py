class Solution:
    # @return an integer
    def atoi(self, str):
        int_max = 2147483647
        int_min = -2147483648
        strng = str.strip()
        if not strng:
            return 0 
        sgn =  1
        i = 0
        if strng[0] == '+':
            i = i + 1
        if strng[0] == '-':
            sgn = sgn*(-1)
            i = i + 1
        strng = strng[i:]
        i = 0
        stop = False
        num_str = ''
        while i < len(strng) and not stop:
            if strng[i] in ['0','1','2','3','4','5','6','7','8','9']:
                num_str = num_str + strng[i]
                i = i + 1
            else:
                stop = True
        if num_str:
            result = int(num_str)*sgn
            if result>int_max:
                return int_max
            if result < int_min:
                return int_min
            return result
        return 0
