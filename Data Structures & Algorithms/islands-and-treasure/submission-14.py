class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        R, C = len(grid), len(grid[0])

        d = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    d.append([r, c])

        dist = 0
        while d:
            new_d = deque()
            while d:
                r, c = d.popleft()
                if r < 0 or r == R or c < 0 or c == C or grid[r][c] < 0:
                    continue

                if dist == 0 or dist < grid[r][c]:
                    grid[r][c] = dist
                    for i, j in [[1,0],[0,1],[0,-1],[-1,0]]:
                        new_d.append([r + i, c + j])
            d = new_d
            dist += 1