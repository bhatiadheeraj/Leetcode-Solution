class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        explore = deque()
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] != 0:
                    mat[row][col] = -1
                else:
                    explore.append((row,col))
        
        directions = [(1,0), (0,1), (0,-1), (-1,0)]

        while explore:
            i,j = explore.popleft()
            for row, col in directions:
                next_row = i + row
                next_col = j + col

                if (0 <= next_row < rows and 0 <= next_col < cols and mat[next_row][next_col] == -1):
                    mat[next_row][next_col] = mat[i][j] + 1
                    explore.append((next_row,next_col))
        return mat
            