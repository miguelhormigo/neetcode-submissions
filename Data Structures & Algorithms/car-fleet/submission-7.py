class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_to_s = {}
        for i in range(len(position)):
            p_to_s[position[i]] = speed[i]
        
        position.sort()

        turns = []
        for i in range(len(position)):
            p = position[i]
            turns.append((target - p) / p_to_s[p])

        groups = 1
        last = turns.pop()
        while len(turns) > 0:
            if last >= turns[-1]:
                turns.pop()
            else:
                groups += 1
                last = turns.pop()
        
        return groups