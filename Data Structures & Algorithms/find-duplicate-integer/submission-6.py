class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while slow == 0 or slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        
        slow = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow