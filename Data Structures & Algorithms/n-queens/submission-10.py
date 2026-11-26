class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        visited = set()

        def is_valid(cur, c):
            row = len(cur) - 2
            l = cur[-1] - 1
            r = cur[-1] + 1
            
            while row >= 0:
                if l >= 0 and cur[row] == l or r < n and cur[row] == r:
                    return False
                l -= 1
                r += 1
                row -= 1
            
            return True
        
        def save_res(cur):
            sol = []
            for r in cur:
                sol.append('.' * r + 'Q' + '.' * (n - r - 1))
            res.append(sol)

        def dfs(i, cur):
            if i == n:
                save_res(cur)
                return
            
            for c in range(n):
                if c in visited:
                    continue

                cur.append(c)
                visited.add(c)
                if is_valid(cur, c):
                    dfs(i + 1, cur)
                cur.pop()
                visited.remove(c)
        
        dfs(0, [])
        return res