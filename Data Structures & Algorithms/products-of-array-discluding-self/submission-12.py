class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)
        for i in range(1, len(nums)):
            sol[i] = sol[i - 1] * nums[i - 1]
        
        carry = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            sol[i] *= carry
            carry *= nums[i]
        
        return sol