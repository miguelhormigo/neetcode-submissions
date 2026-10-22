class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        DIRS = [[1,0],[-1,0],[0,1],[0,-1]]
        to_visit = deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    for i, j in DIRS:
                        to_visit.append([r + i, c + j, 1])
        
        while to_visit:
            r, c, d = to_visit.popleft()
            if r < 0 or r == R or c < 0 or c == C or grid[r][c] != 2147483647:
                continue

            grid[r][c] = d

            for i, j in DIRS:
                to_visit.append([r + i, c + j, d + 1])