class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append([row,col])
                else:
                    mat[row][col] = float('-inf')

        directions = [(0,-1), (1,0), (0,1), (-1,0)]
        while queue:
            i, j = queue.popleft()
            for direction in directions:
                neighbor_x,neighbor_y = i + direction[0], j +direction[1]
                if 0 <= neighbor_x < rows and 0 <= neighbor_y < cols and mat[neighbor_x][neighbor_y] == float('-inf'):
                    mat[neighbor_x][neighbor_y] = mat[i][j] + 1
                    queue.append((neighbor_x,neighbor_y ))
                
        return mat