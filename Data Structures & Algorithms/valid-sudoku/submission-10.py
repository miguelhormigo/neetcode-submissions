class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [0] * 9

        for r in range(9):
            row = 0
            if r % 3 == 0:
                squares = [0] * 9

            for c in range(9):
                if board[r][c] != '.':
                    d = 1 << int(board[r][c])
                    if d & row or d & columns[c] or d & squares[c // 3]:
                        return False
                    
                    row |= d
                    columns[c] |= d
                    squares[c // 3] |= d
        
        return True