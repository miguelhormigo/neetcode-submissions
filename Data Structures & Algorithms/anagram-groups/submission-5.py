class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        sorted_keys = {}

        for w in strs:
            found = False
            ord_w = ''.join(sorted(w))
            if ord_w in sorted_keys:
                found = True
                results[sorted_keys[ord_w]].append(w)
            if not found:
                sorted_keys[ord_w] = len(results)
                results.append([w])

        return results