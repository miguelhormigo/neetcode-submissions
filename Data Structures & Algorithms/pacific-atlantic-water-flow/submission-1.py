class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(x, y, visited, prev):
            key = (x, y)
            if x < 0 or x >= R or y < 0 or y >= C or key in visited or heights[x][y] < prev:
                return
            
            visited.add(key)

            for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dfs(x + i, y + j, visited, heights[x][y])
        
        for r in range(R):
            dfs(r, 0, pacific, float('-inf'))
        for c in range(C):
            dfs(0, c, pacific, float('-inf'))
        
        for r in range(R):
            dfs(r, C - 1, atlantic, float('-inf'))
        for c in range(C):
            dfs(R - 1, c, atlantic, float('-inf'))
        
        res = []
        for x, y in pacific:
            if (x, y) in atlantic:
                res.append([x, y])
        return res