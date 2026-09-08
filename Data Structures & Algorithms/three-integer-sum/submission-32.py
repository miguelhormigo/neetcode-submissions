class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sol = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            n = nums[i]
            while l < r:
                s = n + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    sol.append([n, nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while 0 < r and nums[r] == nums[r+1]:
                        r -= 1
        
        return sol