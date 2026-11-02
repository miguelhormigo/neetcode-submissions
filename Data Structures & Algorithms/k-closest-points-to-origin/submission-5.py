import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            dis = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(min_heap, [dis, x, y])
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1:])
        return res