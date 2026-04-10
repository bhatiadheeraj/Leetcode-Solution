class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #prepare the matrix where there is 1 mark it as - and append 0 in queue
        rows = len(mat)
        cols = len(mat[0])
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1:
                    mat[row][col] = -1
                else:
                    q.append((row,col))
        directions = [(-1,0), (0,1), (1,0), (0,-1)]

        while q:
            current_item = q.popleft()
            for direction in directions:
                next_item_row = direction[0] + current_item[0]
                next_item_col = direction[1] + current_item[1]
                if next_item_row >= 0 and next_item_row < rows and next_item_col >= 0 and next_item_col < cols and mat[next_item_row][next_item_col] == -1:
                    mat[next_item_row][next_item_col] =  mat[current_item[0]][current_item[1]] + 1
                    q.append((next_item_row, next_item_col))
        

        return mat
