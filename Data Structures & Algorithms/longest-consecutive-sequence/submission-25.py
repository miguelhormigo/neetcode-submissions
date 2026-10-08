class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seqs = {}

        for n in nums:
            if n not in seqs:
                length = 1 + seqs.get(n-1, 0) + seqs.get(n+1, 0)
                res = max(res, length)

                seqs[n] = length
                if n-1 in seqs:
                    seqs[n-seqs[n-1]] = length
                if n+1 in seqs:
                    seqs[n+seqs[n+1]] = length
        
        return res