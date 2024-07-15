class Solution(object):
    def solveSudoku(self, board):
        def is_valid(board, row, col, num):
            for x in range(9):
                if board[row][x] == num:
                    return False
            
            for x in range(9):
                if board[x][col] == num:
                    return False
            
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            
            return True
        
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in '123456789':
                            if is_valid(board, i, j, num):
                                board[i][j] = num
                                if solve(board):
                                    return True
                                board[i][j] = '.'
                        return False
            return True
        
        solve(board)
