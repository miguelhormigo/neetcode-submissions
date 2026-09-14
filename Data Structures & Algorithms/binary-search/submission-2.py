class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            n = nums[mid]
            if n < target:
                l = mid + 1
            elif n > target:
                r = mid - 1
            else:
                return mid
        
        return -1