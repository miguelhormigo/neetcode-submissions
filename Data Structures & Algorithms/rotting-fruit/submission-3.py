class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_c = rotten_c = 0
        rotting = deque()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_c += 1
                elif grid[r][c] == 2:
                    rotten_c += 1
                    rotting.append([r, c])
                    visited.add((r, c))
        
        if rotten_c == 0:
            if fresh_c > 0:
                return -1
            return 0

        mins = -1
        fresh_c += rotten_c
        to_rot = deque()
        while rotting or to_rot:
            while rotting:
                r, c = rotting.popleft()
                grid[r][c] = 2
                fresh_c -= 1

                # probar con grid ri cj == 1
                for i, j in [[0,1],[0,-1],[1,0],[-1,0]]:
                    ri, cj = r+i, c+j
                    if 0 <= ri < len(grid) and 0 <= cj < len(grid[0]) and grid[ri][cj] != 0 and (ri, cj) not in visited:
                        to_rot.append([ri, cj])
                        visited.add((ri, cj))

            rotting = to_rot.copy()
            to_rot = deque()
            mins += 1

        return mins if fresh_c == 0 else -1