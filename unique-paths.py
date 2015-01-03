class Solution:
    # @return an integer
    # this is a very obvious dynamic programming problem 
    def uniquePaths(self, m, n):
        matrix = [[1 for j in range(n)] for i in range(m)]   # initialized paths matrix
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
        return matrix[m-1][n-1]
