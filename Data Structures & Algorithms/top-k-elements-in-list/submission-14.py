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
            for n in freqs[i]:
                sol.append(n)
                k -= 1
                if k == 0:
                    return sol
                