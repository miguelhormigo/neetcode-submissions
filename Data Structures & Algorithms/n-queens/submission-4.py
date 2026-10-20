class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, cur = [], []
        visited = set()

        def backtrack(i):
            if i == n:
                res.append(self.get_arr(cur, n))
                return
            
            for j in range(n):
                if j in visited:
                    continue

                cur.append(j)
                visited.add(j)
                if self.is_valid(cur, n):
                    backtrack(i + 1)
                cur.pop()
                visited.remove(j)
        
        backtrack(0)
        return res
    
    def is_valid(self, board, n):
        r, c = len(board) - 2, board[-1] - 1
        while r >= 0 and c >= 0:
            if board[r] == c:
                return False
            r -= 1
            c -= 1
        
        r, c = len(board) - 2, board[-1] + 1
        while r >= 0 and c < n:
            if board[r] == c:
                return False
            r -= 1
            c += 1
        
        return True
    
    def get_arr(self, board, n):
        res = []
        for r in board:
            res.append('.' * r + 'Q' + '.' * (n - r - 1))
        return res