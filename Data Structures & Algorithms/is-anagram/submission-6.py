class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        ls, lt = [0 for _ in range(26)], [0 for _ in range(26)]

        for c in s:
            ls[ord(c) - ord('a')] += 1
        
        for c in t:
            lt[ord(c) - ord('a')] += 1
        
        for i in range(len(lt)):
            if lt[i] != ls[i]:
                return False
        return True