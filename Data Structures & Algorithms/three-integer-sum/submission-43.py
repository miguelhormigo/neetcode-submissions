class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        i = 0

        while i <= len(nums) - 3:
            l, r = i + 1, len(nums) - 1

            while l < r:
                csum = nums[i] + nums[l] + nums[r]

                if csum == 0:
                    sol.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    r -= 1
                elif csum < 0:
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                else:
                    r -= 1
            
            i += 1
            while nums[i] == nums[i - 1] and i < len(nums) - 1:
                i += 1
        
        return sol