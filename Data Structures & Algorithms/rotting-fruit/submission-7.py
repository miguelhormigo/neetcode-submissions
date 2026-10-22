class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        DIRS = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        fresh = 0
        res = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    for i, j in DIRS:
                        q.append([r + i, c + j, 1])
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q:
            r, c, d = q.popleft()
            if r < 0 or r == R or c < 0 or c == C or grid[r][c] != 1:
                continue
            
            grid[r][c] = 2
            fresh -= 1
            res = max(res, d)

            for i, j in DIRS:
                q.append([r + i, c + j, d + 1])
            
        if fresh > 0:
            return -1
        return res