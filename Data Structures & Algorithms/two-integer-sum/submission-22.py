class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j, snums = 0, len(nums) - 1, sorted(nums)

        while i < j:
            s = snums[i] + snums[j]
            if s == target:
                i, j = snums[i], snums[j]
                break
            elif s < target:
                i += 1
            else:
                j -= 1

        soli = solj = None
        for p in range(len(nums)):
            n = nums[p]
            if soli == None and n == i:
                soli = p
            elif solj == None and n == j:
                solj = p
        
        if soli < solj:
            return [soli, solj]
        return [solj, soli]