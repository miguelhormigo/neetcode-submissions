class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        right_max = [len(heights)] * len(heights)
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                right_max[stack.pop()] = i
            stack.append(i)
        
        stack = []
        left_max = [-1] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                left_max[stack.pop()] = i
            stack.append(i)
        
        sol = 0
        for i, h in enumerate(heights):
            area = (right_max[i] - left_max[i] - 1) * h
            sol = max(sol, area)
        return sol