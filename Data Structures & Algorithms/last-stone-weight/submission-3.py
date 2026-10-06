import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for s in stones:
            heapq.heappush(max_heap, -s)
        
        while len(max_heap) > 1:
            a, b = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            if a != b:
                heapq.heappush(max_heap, -abs(a-b))
        
        return -max_heap[-1] if len(max_heap) > 0 else 0