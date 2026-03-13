class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        rows = len(mat)
        cols = len(mat[0])

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] !=0:
                    mat[row][col] = float('inf')
                else:
                    q.append((row,col))

        directions = [(-1,0), (0, 1), (1 , 0), (0,-1)]
        while q:
            i,j = q.popleft()
            for direction in directions:
                n_row = i + direction[0]
                n_col = j + direction[1]
                if n_row >= 0 and n_row < rows and 0 <= n_col < cols and mat[n_row][n_col] == float('inf'):
                    mat[n_row][n_col] = mat[i][j] + 1 
                    q.append((n_row,n_col))
        
        return mat