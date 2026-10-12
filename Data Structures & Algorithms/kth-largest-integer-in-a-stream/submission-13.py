class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_stack = []

        for n in nums:
            if len(self.min_stack) < k:
                heapq.heappush(self.min_stack, n)
            elif n > self.min_stack[0]:
                heapq.heappop(self.min_stack)
                heapq.heappush(self.min_stack, n)

    def add(self, val: int) -> int:
        if len(self.min_stack) < self.k:
            heapq.heappush(self.min_stack, val)
        elif val > self.min_stack[0]:
            heapq.heappop(self.min_stack)
            heapq.heappush(self.min_stack, val)
        
        return self.min_stack[0]