class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        unique = []

        for w in strs:
            found = False
            ord_w = sorted(w)
            for i in range(len(unique)):
                if unique[i] == ord_w:
                    found = True
                    results[i].append(w)
            if not found:
                results.append([w])
                unique.append(ord_w)

        return results