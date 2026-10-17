class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        MOVES = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        d = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = d

                for i, j in MOVES:
                    ri, cj = r+i, c+j
                    if 0 <= ri < len(grid) and 0 <= cj < len(grid[0]) and grid[ri][cj] != -1 and (ri, cj) not in visited:
                        q.append([ri, cj])
                        visited.add((ri, cj))
            d += 1