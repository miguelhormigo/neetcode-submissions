class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        blockers, blockers_c = defaultdict(list), [0] * numCourses
        for c, b in prerequisites:
            blockers[b].append(c)
            blockers_c[c] += 1
        
        q = deque()
        for c in range(numCourses):
            if blockers_c[c] == 0:
                q.append(c)
        
        free = 0
        res = []
        while q:
            c = q.popleft()
            free += 1
            res.append(c)
            for b in blockers[c]:
                blockers_c[b] -= 1
                if blockers_c[b] == 0:
                    q.append(b)
        
        if free == numCourses:
            return res
        return []