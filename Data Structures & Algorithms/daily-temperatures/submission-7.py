class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res, stack = [0] * len(temperatures), []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                l = stack.pop()
                res[l] = i - l
            
            stack.append(i)
        
        return res