class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                row = matrix[mid]
                l, r = 0, len(matrix[0]) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if target > row[mid]:
                        l = mid + 1
                    elif target < row[mid]:
                        r = mid - 1
                    else:
                        return True
        
        return False