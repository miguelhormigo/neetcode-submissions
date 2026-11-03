class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or x >= R or y < 0 or y >= C or board[x][y] in ['X', 'B']:
                return
            
            board[x][y] = 'B'

            for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dfs(x + i, y + j)
        
        for r in range(R):
            dfs(r, 0)
            dfs(r, C - 1)
        
        for c in range(C):
            dfs(0, c)
            dfs(R - 1, c)
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'B':
                    board[r][c] = 'O'