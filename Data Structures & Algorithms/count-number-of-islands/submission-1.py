class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def mark_island(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != '1':
                return
            
            grid[r][c] = '2'
            for i, j in [[0,1],[0,-1],[-1,0],[1,0]]:
                mark_island(r+i, c+j)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    count += 1
                    mark_island(r, c)
        
        return count