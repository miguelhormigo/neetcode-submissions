class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}
        solutions = []

        for s in strs:
            key = [0] * 26
            for l in s:
                key [ord(l) - ord('a')] += 1
            key = str(key)
            
            if key in keys:
                solutions[keys[key]].append(s)
            else:
                keys[key] = len(solutions)
                solutions.append([s])
        
        return solutions