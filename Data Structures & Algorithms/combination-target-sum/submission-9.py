class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(cur, cur_sum, i):
            if cur_sum == target:
                res.append(cur.copy())
                return
            if cur_sum > target or i == len(nums):
                return
            
            cur.append(nums[i])
            dfs(cur, cur_sum + nums[i], i)
            cur.pop()

            dfs(cur, cur_sum, i + 1)
        
        dfs([], 0, 0)
        return res