class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(cur, i):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            if not (i > 0 and nums[i] == nums[i - 1] and len(cur) > 0 and cur[-1] == nums[i]):
                dfs(cur, i + 1)

            cur.append(nums[i])
            dfs(cur, i + 1)
            cur.pop()
        
        dfs([], 0)
        return res