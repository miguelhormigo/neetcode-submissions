class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        while fast == 0 or fast != slow:
            slow, fast = nums[slow], nums[nums[fast]]
        
        slow = 0
        while fast != slow:
            slow, fast = nums[slow], nums[fast]
        
        return slow