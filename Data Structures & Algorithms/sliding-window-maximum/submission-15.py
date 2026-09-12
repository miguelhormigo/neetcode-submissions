from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window, sol = deque(), []
        l = 0

        for r, n in enumerate(nums):
            if r >= k:
                sol.append(window.popleft())
                l += 1
            
            i = 1
            while i <= len(window) and n > window[-i]:
                window[-i] = n
                i += 1
            
            window.append(n)
        
        sol.append(window[0])
        
        return sol