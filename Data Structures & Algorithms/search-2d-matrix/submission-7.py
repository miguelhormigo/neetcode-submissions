class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        total = m * n
        l, r = 0, total - 1

        while l <= r:
            mid = (l + r) // 2
            row, col = mid // n, mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False