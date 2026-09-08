class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        avail = set(nums)
        heads = set()
        max_l = 0
        for n in nums:
            if n - 1 not in avail:
                c = 1
                while n + 1 in avail:
                    n += 1
                    c += 1
                max_l = max(max_l, c)

        return max_l