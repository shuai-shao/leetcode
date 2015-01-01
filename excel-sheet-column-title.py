class Solution:
    # @return a string
    def convertToTitle(self, num):
        if num == 0:
            s = ''
        else:
            s = self.convertToTitle((num-1)//26) + chr((num-1)%26 + ord('A'))
        return s
