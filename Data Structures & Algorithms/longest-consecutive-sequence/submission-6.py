class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        starts = set()

        for n in nums_set:
            if not n-1 in nums_set:
                starts.add(n)
        
        r = 0
        for n in starts:
            c = 0
            while n in nums_set:
                c += 1
                n += 1
            r = max(r, c)
        
        return r