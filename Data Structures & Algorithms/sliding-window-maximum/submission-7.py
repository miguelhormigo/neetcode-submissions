class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        result = []

        for r, n in enumerate(nums):
            if r >= k:
                result.append(window.popleft())
            window.append(n)
            i = len(window) - 2
            while i >= 0 and window[i] < n:
                window[i] = n
                i -= 1
        
        result.append(window.popleft())
        
        return result