class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol, cur = [], []

        def backtrack(i):
            if i == len(s):
                sol.append(cur.copy())
                return
            
            for j in range(i+1, len(s)+1):
                if is_pal(s[i:j]):
                    cur.append(s[i:j])
                    backtrack(j)
                    cur.pop()
        
        def is_pal(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        backtrack(0)
        return sol