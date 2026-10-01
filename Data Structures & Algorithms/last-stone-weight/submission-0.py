import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) >= 2:
            a, b = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            if a != b:
                heapq.heappush(max_heap, -abs(a - b))
        
        return -max_heap[0] if max_heap else 0