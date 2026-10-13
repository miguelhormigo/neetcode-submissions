class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()

        def backtrack(r, c, p):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or p >= len(word) or board[r][c] != word[p] or (r,c) in seen:
                return False
            if p == len(word) - 1:
                print('t')
                return True
            
            seen.add((r,c))
            for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if backtrack(r + i, c + j, p + 1):
                    return True
            seen.remove((r,c))
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                sol = backtrack(r, c, 0)
                if sol:
                    return True
        return False