class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            count = tuple(count)
            if count in results:
                results[count].append(s)
            else:
                results[count] = [s]
        
        return list(results.values())