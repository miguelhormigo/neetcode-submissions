class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[l] < nums[r]:
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            else:
                if nums[m] >= nums[l]:
                    if nums[m] == target:
                        return m
                    elif nums[m] > target and nums[l] <= target:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    if nums[m] == target:
                        return m
                    elif nums[m] < target and nums[r] >= target:
                        l = m + 1
                    else:
                        r = m - 1
        
        return -1