class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        longest = 1

        for n in nums:
            if n-1 not in nums:
                cur = 1
                while n+cur in nums:
                    cur += 1
                longest = max(longest, cur)
        
        return longest