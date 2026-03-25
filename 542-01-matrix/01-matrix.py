class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #lets prepare the matri for reslt 
        q = deque()
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1
        
        directions = [(-1,0) , (1,0), (0,1), (0,-1)]

        while q:
            i,j = q.popleft()
            for direction in directions:
                next_row = direction[0] + i 
                next_col = direction[1] + j 
                if next_row >= 0 and next_row < rows and next_col >= 0 and next_col < cols and mat[next_row][next_col] == -1:
                    mat[next_row][next_col] = mat[i][j] + 1
                    q.append((next_row, next_col))
        
        return mat