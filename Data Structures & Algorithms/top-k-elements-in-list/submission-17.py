class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        freqs = [[] for _ in range(len(nums) + 1)]
        for n in count:
            freqs[count[n]].append(n)
        
        res = []
        for i in range(len(freqs) - 1, -1, -1):
            if freqs[i] != []:
                res.extend(freqs[i])
            if k - len(res) == 0:
                break
        return res