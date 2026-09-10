class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol_pos, sol = {}, []

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)

            if key in sol_pos:
                sol[sol_pos[key]].append(s)
            else:
                sol_pos[key] = len(sol)
                sol.append([s])
        
        return sol