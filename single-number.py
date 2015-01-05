#######################################################################################
# bitwise operation 
#Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        r = 0
        for i in A:
            r = r ^ i    # 'bitwise exclusive or': Each bit is the same if that bit in y is 0, and the complement otherwise
        return r


#######################################################################################
# use the power of Python
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        return 2*sum(set(A)) - sum(A)
        
#######################################################################################
