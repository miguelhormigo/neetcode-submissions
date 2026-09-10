class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for n in count:
            bucket[count[n]].append(n)
        
        sol = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i] != []:
                sol.extend(bucket[i])
                k -= len(bucket[i])
                if k == 0:
                    break
        return sol