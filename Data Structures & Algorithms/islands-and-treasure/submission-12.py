class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        
        q = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append([r, c, 0])

        while q:
            r, c, v = q.popleft()
            if v == 0 or grid[r][c] > v:
                grid[r][c] = v
                for i, j in [[1,0],[0,1],[-1,0],[0,-1]]:
                    nr = r + i
                    nc = c + j
                    if nr >= 0 and nc >= 0 and nr < R and nc < C and grid[nr][nc] > 0:
                        print('\t+')
                        q.append([nr, nc, v + 1])