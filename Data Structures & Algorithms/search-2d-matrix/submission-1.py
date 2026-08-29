class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break
            
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[m][mid]:
                l = mid + 1
            elif target < matrix[m][mid]:
                r = mid - 1
            else:
                return True
        return False