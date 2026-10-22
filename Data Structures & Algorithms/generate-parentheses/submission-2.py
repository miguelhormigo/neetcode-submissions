class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r, cur = [], []

        def backtrack(left, right):
            if left == 0 and right == 0:
                r.append(''.join(cur))
                return
            
            if left:
                cur.append('(')
                backtrack(left - 1, right)
                cur.pop()

            if right > left:
                cur.append(')')
                backtrack(left, right - 1)
                cur.pop()
        
        backtrack(n, n)
        return r