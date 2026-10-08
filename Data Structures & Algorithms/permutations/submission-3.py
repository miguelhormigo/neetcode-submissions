class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, i, cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                cur.append(nums[i])
                backtrack(nums, i+1, cur)
                nums[i], nums[j] = nums[j], nums[i]
                cur.pop()
        
        backtrack(nums, 0, [])
        return res