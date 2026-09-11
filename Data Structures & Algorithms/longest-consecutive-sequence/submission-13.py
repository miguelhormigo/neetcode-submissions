class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)
        beginnings = set()

        for n in nums:
            if n - 1 not in nums_s:
                beginnings.add(n)
        
        max_l = 0
        for n in beginnings:
            count = 1
            while n + 1 in nums_s:
                n += 1
                count += 1
            max_l = max(max_l, count)
        
        return max_l