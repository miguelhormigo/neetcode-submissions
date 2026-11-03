class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        travels, blockers = [[] for _ in range(numCourses)], [0 for _ in range(numCourses)]

        for orig, dest in prerequisites:
            travels[orig].append(dest)
            blockers[dest] += 1
        
        q = deque()
        for c in range(numCourses):
            if blockers[c] == 0:
                q.append(c)
        
        while q:
            c = q.popleft()
            for free_c in travels[c]:
                blockers[free_c] -= 1
                if blockers[free_c] == 0:
                    q.append(free_c)

        for c in blockers:
            if c > 0:
                return False
        return True