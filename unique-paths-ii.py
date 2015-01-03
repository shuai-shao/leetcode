class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        matrix = [[1 for j in range(n)] for i in range(m)]
        
        # assign values for row edge
        first_one = 0
        stop = False
        while not stop and first_one < n:
            if obstacleGrid[0][first_one] == 1:
                stop = True
            first_one += 1
        if stop:
            for j in range(first_one-1,n):
                matrix[0][j] = 0
            
         # assign values for column edge
        first_one = 0
        stop = False
        while not stop and first_one < m:
            if obstacleGrid[first_one][0] == 1:
                stop = True
            first_one += 1
        if stop:
            for i in range(first_one-1,m):
                matrix[i][0] = 0    
            
        # assign values for interior matrix
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
                else:
                    matrix[i][j] = 0
        return matrix[-1][-1]
