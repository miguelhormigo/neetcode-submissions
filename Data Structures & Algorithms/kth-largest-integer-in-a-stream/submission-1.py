import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = []

        for n in nums:
            heapq.heappush(self.max_heap, -n)

    def add(self, val: int) -> int:
        print(self.max_heap)
        heapq.heappush(self.max_heap, -val)

        return -heapq.nsmallest(self.k, self.max_heap)[-1]