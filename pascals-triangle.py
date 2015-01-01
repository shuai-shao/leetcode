class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            pascal = [[1],[1,1]]
            old_list = [1,1]
            for i in range(2,numRows):
                new_list =  [1]
                for j in range(len(old_list)-1):
                    new_list.append(old_list[j]+old_list[j+1])
                new_list.append(1)
                pascal.append(new_list)
                old_list = new_list
        return pascal
