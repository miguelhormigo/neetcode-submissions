class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        if not self.left or num < -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        if abs(len(self.left) - len(self.right)) > 1:
            if len(self.left) < len(self.right):
                heapq.heappush(self.left, -heapq.heappop(self.right))
            else:
                heapq.heappush(self.right, -heapq.heappop(self.left))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        elif len(self.left) < len(self.right):
            return self.right[0]
        elif len(self.left) == 0:
            return
        else:
            return (-self.left[0] + self.right[0]) / 2
        