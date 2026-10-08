class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        avail = set(i for i in range(len(nums)))
        cur = []

        def backtrack(d):
            nonlocal avail

            if not avail:
                res.append(cur.copy())
                return
            
            for i in avail.copy():
                print('\t'*d,nums[i])
                cur.append(nums[i])
                avail.remove(i)
                backtrack(d+1)
                cur.pop()
                avail.add(i)
        
        backtrack(0)
        return res