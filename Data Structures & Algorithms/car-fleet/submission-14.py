class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_to_speed = {position[i]: speed[i] for i in range(len(position))}
        stack = []

        for p in reversed(sorted(position)):
            time = (target - p) / p_to_speed[p]

            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)