class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(s, i, j):
            l, r = i, j
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i, j, cur):
            if j == len(s):
                if i == j:
                    res.append(cur.copy())
                return
            
            dfs(i, j + 1, cur)

            if is_palindrome(s, i, j):
                cur.append(s[i:j+1])
                dfs(j + 1, j + 1, cur)
                cur.pop()
        
        dfs(0, 0, [])
        print(res)
        return res