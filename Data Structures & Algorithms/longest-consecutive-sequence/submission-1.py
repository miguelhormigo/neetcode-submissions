class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        starts = set()

        for n in nums:
            if n-1 not in nums:
                starts.add(n)
        
        longest = cur = 1
        for n in starts:
            while n+1 in nums:
                cur += 1
                n += 1
            longest = max(longest, cur)
            cur = 1
        return longest