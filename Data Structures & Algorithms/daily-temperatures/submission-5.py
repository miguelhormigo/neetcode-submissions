class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                sol[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)
        
        return sol