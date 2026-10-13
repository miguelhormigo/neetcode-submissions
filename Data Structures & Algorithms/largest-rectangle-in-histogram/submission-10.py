class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        LH = len(heights)

        right_max, stack = [LH] * LH, []
        for i in range(LH):
            while stack and heights[i] < heights[stack[-1]]:
                right_max[stack.pop()] = i
            stack.append(i)
        
        left_max, stack = [-1] * LH, []
        for i in range(LH - 1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                left_max[stack.pop()] = i
            stack.append(i)
        
        res = 0
        for i in range(LH):
            area = heights[i] * (right_max[i] - left_max[i] - 1)
            res = max(res, area)
        return res