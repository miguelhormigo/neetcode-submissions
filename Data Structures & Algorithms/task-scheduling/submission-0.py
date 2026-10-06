from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = []
        for task in count:
            heapq.heappush(max_heap, -count[task])
        
        q = deque()
        time = 0

        while max_heap or q:
            time += 1

            if max_heap:
                c = 1 + heapq.heappop(max_heap)
                if c:
                    q.append([c, time + n])
            else:
                time = q[0][1]
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time