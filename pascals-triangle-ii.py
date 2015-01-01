class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            row = [1,1]
            for i in range(1,rowIndex):
                for j in range(len(row)-1):
                    row[j] = row[j] + row[j+1]
                row.insert(0,1)
            return row
       
