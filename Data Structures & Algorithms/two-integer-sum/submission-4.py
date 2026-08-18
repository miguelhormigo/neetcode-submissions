class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = set()

        for i in range(len(nums)):
            if nums[i] in checked:
                continue

            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
                    
            checked.add(nums[i])