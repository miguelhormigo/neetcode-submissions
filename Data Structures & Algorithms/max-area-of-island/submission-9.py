class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1
            for i, j in [[1,0],[0,1],[-1,0],[0,-1]]:
                area += dfs(r+i, c+j)
            return area

        for r in range(R):
            for c in range(C):
                res = max(res, dfs(r, c))
        return res