class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, cur_sum):
            if cur_sum == target:
                res.append(cur.copy())
                return
            if i == len(nums):
                return
            
            new_sum = cur_sum
            while new_sum <= target:
                backtrack(i + 1, cur, new_sum)
                cur.append(nums[i])
                new_sum += nums[i]

            while new_sum > cur_sum:
                cur.pop()
                new_sum -= nums[i]
        
        backtrack(0, [], 0)
        return res