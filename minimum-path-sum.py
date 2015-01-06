class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    # a very typical dynammic programming problem 
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        matrix = [[grid[m-1][n-1] for j in range(n)] for i in range(m)]
        for j in range(n-2,-1,-1):
            matrix[m-1][j] = matrix[m-1][j+1] + grid[m-1][j]
        for i in range(m-2,-1,-1):
            matrix[i][n-1] = matrix[i+1][n-1] + grid[i][n-1]
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                matrix[i][j] = grid[i][j] + min(matrix[i+1][j],matrix[i][j+1])
        return matrix[0][0]
