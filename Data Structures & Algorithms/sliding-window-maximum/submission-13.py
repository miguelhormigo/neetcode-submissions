class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        result = []

        for r, n in enumerate(nums):
            while window and nums[window[-1]] < n:
                window.pop()
            window.append(r)
            
            if window[0] <= r - k:
                window.popleft()

            if r >= k - 1:
                result.append(nums[window[0]])
        
        return result