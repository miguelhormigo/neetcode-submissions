class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]

        for i in range(9):
            row = set()
            if i%3 == 0:
                squares = [set() for _ in range(9)]

            for j in range(9):
                cell = board[i][j]
                if cell != '.':
                    if cell in row or cell in columns[j] or cell in squares[j//3]:
                        return False
                    row.add(cell)
                    columns[j].add(cell)
                    squares[j//3].add(cell)
        
        return True