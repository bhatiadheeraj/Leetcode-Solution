#https://leetcode.com/problems/pascals-triangle/description/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #lets first generate the rows
        pascalContainer = []
        for item in range(1,numRows+1):
            arrayGen = [0] * item
            arrayGen[0] = 1
            #setting last item to 1 
            if len(arrayGen) > 1:arrayGen[-1] = 1
            pascalContainer.append(arrayGen)
        print(pascalContainer)

        for index, item in enumerate(pascalContainer):
            if index >1:
                for idx,value in enumerate(item):
                    if value == 0:
                        #replace with idx-1 + idx of previous item
                        prevRow = pascalContainer[index-1]
                        print(prevRow,item,"prev and current row",idx)
                        newValue = prevRow[idx-1] + prevRow[idx]
                        item[idx] = newValue
        return pascalContainer
