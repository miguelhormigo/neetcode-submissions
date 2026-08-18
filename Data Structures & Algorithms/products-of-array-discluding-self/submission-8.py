class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1] * len(nums)

        for i in range(1, len(nums)):
            prods[i] = prods[i-1] * nums[i-1]

        prod = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            prods[i] *= prod
            prod *= nums[i]

        return prods
