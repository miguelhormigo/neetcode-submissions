class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        vals = []

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)

            if key in res:
                vals[res[key]].append(s)
            else:
                res[key] = len(vals)
                vals.append([s])
        
        return vals