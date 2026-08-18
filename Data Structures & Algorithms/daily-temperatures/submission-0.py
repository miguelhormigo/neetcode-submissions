class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pending = [0]
        r = [0 for _ in range(len(temperatures))]

        for i in range(1, len(temperatures)):
            t = temperatures[i]
            while pending and t > temperatures[pending[-1]]:
                # print(i,t,pending, temperatures[pending[-1]])
                p = pending.pop()
                r[p] = i - p

            pending.append(i)
        
        return r