class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        length = len(num)
        i = 0
        found = False
        
        while found == False:
            target_num = num[i]
            count = 0
            for j in range(length):
                if num[j] == target_num:
                    count = count + 1
            if count > length//2:
                found = True
                integer = target_num
            else:
                i = i + 1
                while num[i] == num[i-1]:
                    i = i + 1
        return integer
