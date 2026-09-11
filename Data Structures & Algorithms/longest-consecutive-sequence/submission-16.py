class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_d = defaultdict(int)
        max_l = 0

        for n in nums:
            if not nums_d[n]:
                nums_d[n] = nums_d[n - 1] + nums_d[n + 1] + 1
                nums_d[n - nums_d[n - 1]] = nums_d[n]
                nums_d[n + nums_d[n + 1]] = nums_d[n]
                max_l = max(max_l, nums_d[n])
        
        return max_l