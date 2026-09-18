class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [0] * 9

        for r in range(9):
            row = 0
            if r % 3 == 0:
                squares = [0] * 3

            for c in range(9):
                v = board[r][c]
                if v == '.':
                    continue
                
                d = 1 << (int(v) - 1)
                if d & row or d & squares[c // 3] or d & columns[c]:
                    return False
                
                row |= d
                squares[c // 3] |= d
                columns[c] |= d
        
        return True