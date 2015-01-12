############################################################################################################
Solution 1 :(dynamic programming)
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len(triangle)
        min_matrix = [[triangle[i][j] for j in range(i+1)] for i in range(n)]    # use deep copy here. shallow copy will cause error
        for i in range(n-1)[::-1]:
            for j in range(i+1):
                min_matrix[i][j] = triangle[i][j] + min(min_matrix[i+1][j], min_matrix[i+1][j+1])
        return min_matrix[0][0]

# deep copy : copy value of each elements
# shallow copy: only copy the structure, the new copy and the old share the elements. One change will cause another change as well.

############################################################################################################
Solution 2: same idea as solution 1, but only use O(n) space, where n is the length of the triangle
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len(triangle)
        temp = [triangle[n-1][i] for i in range(n)]
        for i in range(1,n)[::-1]:
            for j in range(i):
                temp[j] = triangle[i-1][j] + min(temp[j], temp[j+1])
        return temp[0]
            
