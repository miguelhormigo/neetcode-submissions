class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur, left, right):
            if left == right == n:
                res.append(''.join(cur))
                return
            
            if left < n:
                cur.append('(')
                left += 1
                dfs(cur, left, right)
                cur.pop()
                left -= 1

            if left > right:
                cur.append(')')
                right += 1
                dfs(cur, left, right)
                cur.pop()
                right -= 1
        
        dfs([], 0, 0)
        return res