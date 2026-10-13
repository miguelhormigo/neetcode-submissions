class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        if not self.left:
            self.left.append(-num)
        elif num <= -self.left[0]:
            heapq.heappush(self.left, -num)
            if len(self.left) > len(self.right) + 1:
                heapq.heappush(self.right, -heapq.heappop(self.left))
        else:
            heapq.heappush(self.right, num)
            if len(self.left) < len(self.right):
                heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2