class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == R or c == C or grid[r][c] == '0':
                return 0
            
            grid[r][c] = '0'

            for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dfs(r + i, c + j)
            
            return 1
        
        res = 0
        for r in range(R):
            for c in range(C):
                res += dfs(r, c)
        return res