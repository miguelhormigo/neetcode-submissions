class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        for n in count:
            bucket[count[n]].append(n)
        
        sol = []
        i = len(bucket) - 1
        while k:
            if bucket[i]:
                sol.extend(bucket[i])
                k -= len(bucket[i])
            i -= 1
        return sol