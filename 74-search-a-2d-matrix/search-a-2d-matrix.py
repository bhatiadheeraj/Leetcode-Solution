class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        for row in matrix:
            if row[0] > target:
                continue
            else:
                for element in row:
                    if element == target:
                        return True
        return False
                
        