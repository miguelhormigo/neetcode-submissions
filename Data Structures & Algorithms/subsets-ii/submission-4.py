class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, cur, uniq = [], [], set()

        def backtrack(i):
            if i == len(nums):
                key = tuple(cur)
                if key not in uniq:
                    uniq.add(key)
                    res.append(cur.copy())
                return
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                cur.append(nums[j])
                backtrack(j + 1)
                cur.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res