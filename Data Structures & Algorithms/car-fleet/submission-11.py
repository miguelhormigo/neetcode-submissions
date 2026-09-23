class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # order positions in descending order
        speed_map = {}
        for i, p in enumerate(position):
            speed_map[p] = speed[i]
        
        position.sort(reverse=True)
        
        # calculate times to reach target
        turns = []
        for p in position:
            turns.append((target - p) / speed_map[p])
        
        # add n to stack if n > stack[-1]
        stack = []
        for t in turns:
            if not stack or stack[-1] < t:
                stack.append(t)
        
        return len(stack)