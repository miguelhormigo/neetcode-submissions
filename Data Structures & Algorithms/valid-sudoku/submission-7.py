class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [0 for _ in range(9)]
        for r in range(9):
            row = 0
            if r % 3 == 0:
                squares = [0 for _ in range(3)]
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    continue
                v = int(v)

                if 1<<v & row or 1<<v & columns[c] or 1<<v & squares[c // 3]:
                    return False
                
                row |= 1<<v
                columns[c] |= 1<<v
                squares[c // 3] |= 1<<v
        
        return True