class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [0] * 9

        for r in range(9):
            row = 0
            if r % 3 == 0:
                squares = [0] * 3

            for c in range(9):
                d = board[r][c]
                if d != '.':
                    d = 1 << (int(d) - 1)

                    if row & d or columns[c] & d or squares[c//3] & d:
                        return False
                    
                    row |= d
                    columns[c] |= d
                    squares[c//3] |= d
            
        return True