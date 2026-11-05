class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        max_heap = []
        for task in counter:
            heapq.heappush(max_heap, -counter[task])
        
        frozen = deque()
        cycles = 0
        while max_heap or frozen:
            if not max_heap:
                cycles = frozen[0][0]
            while frozen and frozen[0][0] == cycles:
                heapq.heappush(max_heap, -frozen.popleft()[1])
            task = -heapq.heappop(max_heap) - 1
            if task > 0:
                frozen.append([cycles + n + 1, task])
            cycles += 1
        return cycles