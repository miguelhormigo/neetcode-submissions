class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        avail = set(i for i in range(len(nums)))
        cur = []

        def backtrack():
            nonlocal avail

            if not avail:
                res.append(cur.copy())
                return
            
            for i in avail.copy():
                cur.append(nums[i])
                avail.remove(i)
                backtrack()
                cur.pop()
                avail.add(i)
        
        backtrack()
        return res