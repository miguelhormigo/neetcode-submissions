class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        snums = sorted(nums)
        l, r = 0, len(nums) - 1

        while l < r:
            diff = snums[l] + snums[r] - target
            if diff < 0:
                l += 1
            elif diff > 0:
                r -= 1
            else:
                break
        
        results = []
        i = 0
        while len(results) < 2:
            if (l != None and nums[i] == snums[l]) or (r != None and nums[i] == snums[r]):
                results.append(i)
            i += 1
        return results