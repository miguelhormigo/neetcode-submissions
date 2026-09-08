class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        avail = set(nums)

        heads = set()
        for n in nums:
            if n - 1 not in avail:
                heads.add(n)

        max_l = 0
        for h in heads:
            c = 1
            while h + 1 in avail:
                h += 1
                c += 1
            max_l = max(max_l, c)

        return max_l