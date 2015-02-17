class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        length = len(board)
        for i in range(length):
            for j in range(length):
                if not self.check_row(board,i,j):
                    return False
                if not self.check_column(board, i,j):
                    return False
                if not self.check_box(board,i,j):
                    return False
        return True
        
    def check_row(self, board, i, j):
        if board[i][j]!='.':
            for ind in range(j+1,len(board)):
                if board[i][ind] == board[i][j]:
                    return False
        return True
        
    def check_column(self, board, i, j):
        if board[i][j]!='.':
            for ind in range(i+1,len(board)):
                if board[ind][j] == board[i][j]:
                    return False
        return True
    
    def check_box(self, board, i ,j):
        box_row = i//3
        box_column = j//3
        if board[i][j]!='.':
            for ind_row in range(3*(box_row),3*(box_row+1)):
                for ind_column in range(3*(box_column), 3*(box_column+1)):
                    if board[ind_row][ind_column] == board[i][j]:
                        if (ind_row!=i or ind_column!=j):
                            return False
        return True
        
