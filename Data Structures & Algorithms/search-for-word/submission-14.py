class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(p, r, c):
            if p == len(word):
                return True
            if r < 0 or r == ROWS or c < 0 or c == COLS or word[p] != board[r][c] or board[r][c] == '*':
                return
            char = board[r][c]
            board[r][c] = '*'
            print(p, r,c)
            for i, j in [[1,0],[-1,0],[0,1],[0,-1]]:
                if dfs(p + 1, r + i, c + j):
                    return True
            board[r][c] = char
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        return False