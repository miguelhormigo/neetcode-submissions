class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        sol = float('inf')

        while l <= r:
            m = (l + r) // 2

            sol = min(sol, nums[m])
            if nums[l] < nums[r]:
                r = m - 1
            elif nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return sol