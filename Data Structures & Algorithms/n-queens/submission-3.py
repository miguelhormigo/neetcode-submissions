class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sol, cur, locked = [], [], set()

        def backtrack(i):
            if i == n:
                self.save_sol(n, sol, cur)
                return
            for j in range(n):
                if j in locked:
                    continue
                cur.append(j)
                if self.is_valid(n, cur):
                    locked.add(j)
                    backtrack(i + 1)
                    locked.remove(j)
                cur.pop()
        
        backtrack(0)
        return sol

    def is_valid(self, n, cur):
        # check columns
        for row in cur[:-1]:
            if row == cur[-1]:
                return False

        # check diagonals
        r, c = len(cur) - 1 - 1, cur[-1] - 1
        while r >= 0 and c >= 0:
            if cur[r] == c:
                return False
            r -= 1
            c -= 1
        
        r, c = len(cur) - 1 - 1, cur[-1] + 1
        while r >= 0 and c < n:
            if cur[r] == c:
                return False
            r -= 1
            c += 1

        return True
    
    def save_sol(self, n, sol, cur):
        board = []
        for r in cur:
            row = []
            row.append('.' * r)
            row.append('Q')
            row.append('.' * (n - r - 1))
            board.append(''.join(row))
        sol.append(board)