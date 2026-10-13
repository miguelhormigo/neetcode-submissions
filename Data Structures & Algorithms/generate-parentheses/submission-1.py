class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []

        def backtrack(cur, left, right):
            if left == right == 0:
                sol.append(''.join(cur))
                return
            if left > 0:
                cur.append('(')
                backtrack(cur, left - 1, right)
                cur.pop()
            if right > left:
                cur.append(')')
                backtrack(cur, left, right - 1)
                cur.pop()
        
        backtrack([], n, n)
        return sol