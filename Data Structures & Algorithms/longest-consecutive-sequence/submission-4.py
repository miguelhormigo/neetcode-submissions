class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        starts = set()

        for n in nums_set:
            if n-1 not in nums_set:
                starts.add(n)
        
        max_l, max_n = 0, None
        for s in starts:
            nxt = s+1
            cur_l = 1
            while nxt in nums_set:
                nxt += 1
                cur_l += 1
            if cur_l > max_l:
                max_l = cur_l
                max_n = s
        
        return max_l