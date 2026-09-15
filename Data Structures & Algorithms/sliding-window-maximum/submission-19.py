from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sol = []
        d = deque()
        l = 0

        for r, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d.append(r)

            if r >= k - 1:
                l += 1
                sol.append(nums[d[0]])
                if d[0] < l:
                    d.popleft()
        
        return sol