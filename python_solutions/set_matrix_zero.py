#Set Matrix Zeroes
#https://leetcode.com/problems/set-matrix-zeroes/editorial/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        R = len(matrix) #len of rows
        C = len(matrix[0]) #len of cols
        rows, col = set(),set()

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    print(i,j)
                    rows.add(i)
                    col.add(j)
        
        print("NOW I am checking")
        for i in range(R):
            for j in range(C):
                if i in rows or j in col:
                    print(i,j)
                    matrix[i][j] = 0

        print(R)
        print(C)
        print(matrix,matrix[0])

    
def replaceColoumn(self,index,matrix):
    for row in matrix:
        row[index] = 0
    return matrix

def replaceRow(self,row):
    length_of_row = len(row)
    print("Inside Replace row",len(row))
    return [0] * length_of_row
