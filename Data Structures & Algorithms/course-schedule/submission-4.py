class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        blockers, blockers_c = defaultdict(list), [0] * numCourses
        for c, b in prerequisites:
            blockers[b].append(c)
            blockers_c[c] += 1
        
        free = 0
        q = deque()
        for c in range(numCourses):
            if blockers_c[c] == 0:
                q.append(c)
                free += 1
        
        while q:
            c = q.popleft()
            for d in blockers[c]:
                blockers_c[d] -= 1
                if blockers_c[d] == 0:
                    q.append(d)
                    free += 1
        
        if free == numCourses:
            return True
        return False