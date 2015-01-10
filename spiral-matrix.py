class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return [matrix[0][j] for j in range(n)]
        if n == 1:
            return [matrix[i][0] for i in range(m)]
        # now if m >= 2 and n >= 2:
        result = matrix[0][:] + [matrix[i][n-1] for i in range(1,m)] +  [matrix[m-1][i]for i in range(n-1)[::-1]] +[matrix[i][0] for i in range(1,m-1)[::-1]]
        result = result + self.spiralOrder([[matrix[i][j] for j in range(1,n-1)] for i in range(1,m-1)])
        return result        
