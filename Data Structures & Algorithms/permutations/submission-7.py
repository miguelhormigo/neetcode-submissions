class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, i):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                cur[i], cur[j] = cur[j], cur[i]
                dfs(cur, i + 1)
                cur[i], cur[j] = cur[j], cur[i]
        
        dfs(nums, 0)
        return res