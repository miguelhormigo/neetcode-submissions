from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        freq = [[] for _ in range(len(nums)+1)]
        for n in counter:
            freq[counter[n]].append(n)
        
        sols = []
        i = len(freq) - 1
        while k > 0:
            if len(freq[i]) > 0:
                sols.extend(freq[i])
                k -= len(freq[i])
            i -= 1
        
        return sols