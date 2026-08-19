class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for r, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()
            q.append(r)

            if q[0] <= r - k:
                q.popleft()

            if r >= k - 1:
                res.append(nums[q[0]])

        return res