class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        q = []
        left = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    left += 1
        
        if left == 0:
            return 0
            
        time = -1
        while q and left:
            new_q = []
            while q:
                r, c = q.pop()
                if grid[r][c] == 1:
                    left -= 1
                grid[r][c] = 2
                for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    ri, cj = r + i, c + j
                    if ri >= 0 and ri < R and cj >= 0 and cj < C and grid[ri][cj] == 1:
                        new_q.append([ri, cj])
            q = new_q
            time += 1
        
        if left == 0:
            return time
        return -1