class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]

        for r in range(9):
            if r%3 == 0:
                squares = [set() for _ in range(3)]

            row = board[r]
            row_set = set()
            for c in range(9):
                cell = row[c]
                if cell == '.':
                    continue
                if cell in row_set or cell in columns[c] or cell in squares[c//3]:
                    return False
                row_set.add(cell)
                columns[c].add(cell)
                squares[c//3].add(cell)
        
        return True