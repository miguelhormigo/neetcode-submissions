import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for n in nums:
            heapq.heappush(self.min_heap, n)
        
        # while len(self.min_heap) >= self.k:
            # heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        # if len(self.min_heap) >= self.k:
            # return heapq.heappop(self.min_heap)
        # else:
            # return heap[0]
        return heapq.nlargest(self.k, self.min_heap)[-1]