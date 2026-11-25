class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(cur, cur_sum, i):
            if cur_sum == target:
                res.append(cur.copy())
                return
            if cur_sum > target or i == len(nums):
                return
            
            dfs(cur, cur_sum, i + 1)

            c = 0
            new_sum = cur_sum
            while new_sum < target:
                cur.append(nums[i])
                new_sum += nums[i]
                dfs(cur, new_sum, i + 1)
                c += 1
            while c:
                cur.pop()
                c -= 1
        
        dfs([], 0, 0)
        return res