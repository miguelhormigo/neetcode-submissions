from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap, cache = [], {}
        for point in points:
            dist = sqrt(point[0]**2 + point[1]**2)
            if dist in cache:
                cache[dist].append(point)
            else:
                heapq.heappush(min_heap, dist)
                cache[dist] = [point]
        
        print(min_heap, cache)
        res = []
        c = 0
        while c < k:
            print(c, cache[min_heap[0]])
            vals = cache[heapq.heappop(min_heap)]
            c += len(vals)
            res.extend(vals)
        return res