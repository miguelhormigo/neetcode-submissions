class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        chars = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        sol, comb = [], []

        def backtrack(i):
            if i == len(digits):
                sol.append(''.join(comb))
                return
            for c in chars[digits[i]]:
                comb.append(c)
                backtrack(i + 1)
                comb.pop()
        
        backtrack(0)
        return sol