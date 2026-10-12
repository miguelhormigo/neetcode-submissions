class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            v = [math.sqrt(x**2 + y**2), x, y]
            heapq.heappush(min_heap, v)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1:])
        return res