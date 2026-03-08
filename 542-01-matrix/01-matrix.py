class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #prepare the matrix and bfs :) 
        queue = deque()
        #mark the ones for bfs search and put the others in queue for exploration 
        rows = len(mat)
        cols = len(mat[0])

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row,col))
                else:
                    mat[row][col] = float('-inf')
        
        directions = [(0,-1), (1,0), (0,1), (-1,0)]

        while queue:
            i,j = queue.popleft()
            for direction in directions:
                next_row = i + direction[0]
                next_col = j + direction[1]

                if 0 <= next_row < rows and 0 <= next_col < cols and mat[next_row][next_col] == float('-inf'):
                    mat[next_row][next_col] = mat[i][j] + 1
                    queue.append((next_row, next_col))

        return mat 