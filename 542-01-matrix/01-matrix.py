class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        rows, cols = len(mat), len(mat[0])

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] ==0:
                    queue.append((row,col))
                else:
                    mat[row][col] = float('inf')
        print(mat)
        directions = [(-1,0), (0,1), (1,0), (0,-1)]

        while queue:
            i,j = queue.popleft()
            print(mat[i][j], i,j)
            for col,row in directions:
                next_row = i + row
                next_col = j + col
                if 0<= next_row < rows and 0 <= next_col < cols and mat[next_row][next_col] == float('inf'):
                    mat[next_row][next_col] = mat[i][j] + 1
                    queue.append((next_row, next_col))
        
        return mat
