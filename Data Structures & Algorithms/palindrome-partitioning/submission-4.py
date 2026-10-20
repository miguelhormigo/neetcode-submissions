class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, j, cur):
            if j == len(s):
                if i == j:
                    res.append(cur.copy())
                return
            
            if self.is_pal(s, i, j):
                cur.append(s[i : j + 1])
                backtrack(j + 1, j + 1, cur)
                cur.pop()
            
            backtrack(i, j + 1, cur)
        
        backtrack(0, 0, [])
        return res
        
    def is_pal(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True