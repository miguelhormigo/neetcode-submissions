class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        paths = [[] for _ in range(n)]
        for a, b in edges:
            paths[a].append(b)
            paths[b].append(a)
        
        visited = set()
        left = set()
        for n in range(n):
            left.add(n)
        print(paths)
        def dfs(node, prev):
            print(node, left)

            if node in visited:
                return

            if node in left:
                left.remove(node)
            visited.add(node)
            for neig in paths[node]:
                if neig == prev:
                    continue
                print('\t',neig)
                dfs(neig, node)
        
        count = 0
        while left:
            node = left.pop()
            count += 1
            dfs(node, -1)
        return count