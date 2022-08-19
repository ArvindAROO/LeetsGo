class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(1, len(matrix)):
            if matrix[i][0] < target:
                pass
            else:
                if target in matrix[i - 1]:
                    return True
        if target in matrix[-1]:
            return True
        return False