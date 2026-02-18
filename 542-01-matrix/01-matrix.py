class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1:
                    mat[row][col] = -1
                else:
                    queue.append((row,col))
        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        while queue:
            i,j = queue.popleft()
            for row, col in directions:
                next_row = i+row
                next_col = j + col

                #safe check limits
                if (0 <= next_row < rows and 0 <= next_col < cols and mat[next_row][next_col] == -1):
                    mat[next_row][next_col] = mat[i][j] + 1
                    queue.append((next_row,next_col))
       
        return mat