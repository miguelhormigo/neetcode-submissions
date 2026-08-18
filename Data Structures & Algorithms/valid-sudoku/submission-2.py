class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [0] * 9

        for r in range(9):
            if r%3 == 0:
                squares = [0] * 3

            row = board[r]
            row_int = 0
            for c in range(9):
                cell = row[c]
                if cell == '.':
                    continue
                bit = 1 << (int(cell) - 1)
                if (row_int | columns[c] | squares[c//3]) & bit:
                    return False
                row_int |= bit
                columns[c] |= bit
                squares[c//3] |= bit
        
        return True