class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            a, b = heapq.heappop(max_heap), heapq.heappop(max_heap)
            heapq.heappush(max_heap, a - b)
        
        return -max_heap[0]