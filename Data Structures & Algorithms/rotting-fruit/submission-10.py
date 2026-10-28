class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        fresh = 0
        q = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1

        mins = 0
        while True:
            newq = deque()
            while q:
                r, c = q.popleft()
                for i, j in [[1,0],[0,1],[-1,0],[0,-1]]:
                    x, y = r + i, c + j
                    if x >= 0 and y >= 0 and x < R and y < C and grid[x][y] == 1:
                        newq.append([x, y])
                        grid[x][y] = 2
                        fresh -= 1
            if not newq:
                break
            q = newq
            mins += 1

        if fresh == 0:
            return mins
        return -1