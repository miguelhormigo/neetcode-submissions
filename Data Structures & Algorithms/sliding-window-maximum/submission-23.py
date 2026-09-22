from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        sol = []

        l = 0
        for r, n in enumerate(nums):
            while d and n > nums[d[-1]]:
                d.pop()
            d.append(r)

            if r >= k - 1:
                sol.append(nums[d[0]])
                l += 1
                if l > d[0]:
                    d.popleft()
            
        return sol