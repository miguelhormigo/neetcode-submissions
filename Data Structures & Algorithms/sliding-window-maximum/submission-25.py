class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, stack = [], []
        l = 0

        for r in range(len(nums)):
            if r >= k:
                res.append(nums[stack[0]])

                l += 1
                if stack[0] < l:
                    stack.pop(0)
            
            while stack and nums[r] > nums[stack[-1]]:
                stack.pop()
            stack.append(r)
        
        res.append(nums[stack[0]])
        
        return res