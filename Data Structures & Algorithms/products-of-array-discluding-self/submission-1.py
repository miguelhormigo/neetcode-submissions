class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return

        prods = [nums[0]]
        for i in range(1, len(nums)):
            prods.append(prods[i-1] * nums[i])
        
        prods_rev = [nums[-1]]
        for i in range(1, len(nums)):
            prods_rev.insert(0, prods_rev[-i] * nums[-i-1])
        
        results = []
        for i in range(len(nums)):
            left = prods[i-1] if i > 0 else 1
            right = prods_rev[i+1] if i < len(nums)-1 else 1
            results.append(left * right)
        return results