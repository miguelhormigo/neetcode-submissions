class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        carry = nums[0]
        for i in range(1, len(nums)):
            res[i] *= carry
            carry *= nums[i]

        carry = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] *= carry
            carry *= nums[i]
        return res