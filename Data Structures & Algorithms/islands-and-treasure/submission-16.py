class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        R, C = len(grid), len(grid[0])

        d = []
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    d.append([r, c])

        dist = 0

        while d:
            new_d = []

            while d:
                r, c = d.pop()

                if grid[r][c] == INF:
                    grid[r][c] = dist

                for i, j in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
                    nr, nc = r + i, c + j

                    if (0 <= nr < R and 0 <= nc < C
                        and grid[nr][nc] == INF):
                        grid[nr][nc] = dist + 1
                        new_d.append([nr, nc])

            d = new_d
            dist += 1