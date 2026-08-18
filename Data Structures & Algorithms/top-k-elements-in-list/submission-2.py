from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        
        order = [[] for _ in range(len(nums))]
        for n in count:
            order[count[n]-1].append(n)
        
        results = []
        i = len(order)-1
        while k:
            if order[i]:
                results.extend(order[i])
            k -= len(order[i])
            i -= 1
        return results