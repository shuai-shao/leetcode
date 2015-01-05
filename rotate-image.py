class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    # in-place solution
    def rotate(self, matrix):
        n = len(matrix)
        if n % 2 == 0:
            n_div = n / 2   # if n is even, divide the matrix into four parts evenly 
            for i in range(n_div):
                for j in range(n_div):    # i,j --- n-1-j,i (rotation 90)
                    a = matrix[i][j] 
                    matrix[i][j] = matrix[n-1-j][i]
                    matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                    matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                    matrix[j][n-1-i] = a
                    
        else:
            n_div = (n+1) / 2  # if n is odd, the situation is a bit more complicated, draw a graph to help you understand
            for i in range(n_div-1):
                for j in range(n_div):    # covers all elements in matrix except the center, which will remain unchanged
                    a = matrix[i][j] 
                    matrix[i][j] = matrix[n-1-j][i]
                    matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                    matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                    matrix[j][n-1-i] = a
                    
        return matrix
