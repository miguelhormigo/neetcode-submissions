class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()

        def backtrack(i, r, c):
            if r < 0 or c < 0 or r == len(board) or c == len(board[0]) or board[r][c] != word[i] or (r, c) in seen:
                return False
            if i == len(word) - 1:
                return True


            seen.add((r, c))
            if backtrack(i+1, r+1, c) or backtrack(i+1, r-1, c) or backtrack(i+1, r, c+1) or backtrack(i+1, r, c-1):
                return True
            seen.remove((r, c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(0, r, c):
                    return True
        return False