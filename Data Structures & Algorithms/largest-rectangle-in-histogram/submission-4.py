class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        right_b = [len(heights)] * len(heights)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                right_b[stack.pop()] = i
            stack.append(i)

        stack = []
        left_b = [-1] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                left_b[stack.pop()] = i
            stack.append(i)

        res = 0
        for i in range(len(heights)):
            area = (right_b[i] - left_b[i] - 1) * heights[i]
            res = max(res, area)
        
        return res