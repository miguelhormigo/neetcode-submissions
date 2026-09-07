class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pos, res = {}, []

        for w in strs:
            count = [0] * 26
            for c in w:
                count[ord(c) - ord('a')] += 1
            
            t = tuple(count)
            if t in pos:
                res[pos[t]].append(w)
            else:
                pos[t] = len(res)
                res.append([w])
        
        return res