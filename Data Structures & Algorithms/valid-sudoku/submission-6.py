class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]
        for r in range(9):
            row = set()
            if r % 3 == 0:
                squares = [set() for _ in range(3)]
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    continue
                    
                if v in row or v in columns[c] or v in squares[c // 3]:
                    return False
                
                row.add(v)
                columns[c].add(v)
                squares[c //3 ].add(v)
        
        return True