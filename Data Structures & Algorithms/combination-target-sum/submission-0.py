class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        cur, cur_sum = [], 0

        def backtrack(i):
            nonlocal cur, cur_sum

            if cur_sum == target:
                res.append(cur.copy())
            
            for j in range(i, len(nums)):
                if nums[j] + cur_sum > target:
                    return

                cur.append(nums[j])
                cur_sum += nums[j]

                backtrack(j)

                cur.pop()
                cur_sum -= nums[j]
        
        backtrack(0)
        return res