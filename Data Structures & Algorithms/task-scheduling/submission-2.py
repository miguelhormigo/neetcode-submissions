from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0
        max_heap = []
        counter = Counter(tasks)
        for task in counter:
            heapq.heappush(max_heap, -counter[task])
        
        blocked = deque()
        
        while max_heap or blocked:
            if blocked and blocked[0][0] <= cycles:
                heapq.heappush(max_heap, -blocked.popleft()[1])

            if max_heap:
                task = -heapq.heappop(max_heap) - 1
                if task > 0:
                    blocked.append([cycles + n + 1, task])

            cycles += 1
        
        return cycles