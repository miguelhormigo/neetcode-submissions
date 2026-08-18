class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        starts = set()

        r = 0
        for n in nums_set:
            if not n-1 in nums_set:
                c = 0
                while n in nums_set:
                    c += 1
                    n += 1
                r = max(r, c)
        
        return r