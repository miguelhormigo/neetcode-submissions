class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        available, frozen = [], deque()
        for task in count:
            heapq.heappush(available, -count[task])
        
        cycle = 0
        
        while available or frozen:
            if not available and cycle < frozen[0][0]:
                cycle = frozen[0][0]

            while frozen and frozen[0][0] == cycle:
                heapq.heappush(available, frozen.popleft()[1])

            left = -heapq.heappop(available) - 1
            if left > 0:
                frozen.append([cycle + n + 1, -left])

            cycle += 1
        
        return cycle