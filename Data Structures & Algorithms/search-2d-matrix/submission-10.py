class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        l, r = 0, R * C - 1

        while l <= r:
            m = (l + r) // 2
            row, col = m // C, m % C

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False