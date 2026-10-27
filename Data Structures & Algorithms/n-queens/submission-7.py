class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sol, cur = [], []
        used = set()

        def is_valid():
            r, c = len(cur) - 2, cur[-1] - 1
            while r >= 0 and c >= 0:
                if cur[r] == c:
                    return False
                r -= 1
                c -= 1

            r, c = len(cur) - 2, cur[-1] + 1
            while r >= 0 and c < n:
                if cur[r] == c:
                    return False
                r -= 1
                c += 1

            return True
        
        def append_sol():
            res = []
            for r in cur:
                res.append('.' * r + 'Q' + '.' * (n - r - 1))
            sol.append(res)

        def dfs(i):
            if i == n:
                append_sol()
                return

            for j in range(n):
                if j in used:
                    continue

                cur.append(j)
                used.add(j)
                if is_valid():
                    dfs(i + 1)
                used.remove(j)
                cur.pop()
        
        dfs(0)
        return sol