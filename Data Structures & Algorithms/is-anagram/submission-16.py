class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)
        for c in s:
            seen[c] += 1
        
        for c in t:
            seen[c] -= 1
            if seen[c] == 0:
                del seen[c]
        
        return len(seen.keys()) == 0