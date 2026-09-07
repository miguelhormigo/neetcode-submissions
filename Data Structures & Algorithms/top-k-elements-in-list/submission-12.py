class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        freqs = [[] for _ in range(len(nums))]
        for n in count:
            freqs[count[n] - 1].append(n)
        
        sol = []
        for i in range(len(freqs)-1, -1, -1):
            ns = freqs[i]
            if ns != []:
                sol.extend(ns)
                k -= len(ns)
                if k == 0:
                    return sol