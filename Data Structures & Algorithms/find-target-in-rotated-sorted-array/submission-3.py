class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. Find start
        start, k = nums[0], 0
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < start:
                    start, k = nums[l], l
                break
            
            m = (l + r) // 2
            if nums[m] < start:
                    start, k = nums[m], m
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            mk = (m + k) % len(nums)

            if nums[mk] < target:
                l = m + 1
            elif nums[mk] > target:
                r = m - 1
            else:
                return mk
        
        return -1