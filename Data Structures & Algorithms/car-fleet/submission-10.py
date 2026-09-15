class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_to_s = {}
        for i in range(len(position)):
            p_to_s[position[i]] = speed[i]
        
        position.sort(reverse=True)

        stack = []
        for p in position:
            turns = (target - p) / p_to_s[p]
            if not stack or stack[-1] < turns:
                stack.append(turns)

        return len(stack)