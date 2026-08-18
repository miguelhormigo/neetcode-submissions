class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        keys = {}
        
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in keys:
                results[keys[sorted_s]].append(s)
            else:
                keys[sorted_s] = len(results)
                results.append([s])
        
        return results