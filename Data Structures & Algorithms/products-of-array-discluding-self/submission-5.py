class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return

        prods = [nums[0]]
        for i in range(1, len(nums)):
            prods.append(prods[i-1] * nums[i])
        
        right = 1
        for i in range(1, len(nums)+1):
            left = prods[-i-1] if i < len(nums) else 1
            prods[-i] = left * right
            right *= nums[-i]
        return prods