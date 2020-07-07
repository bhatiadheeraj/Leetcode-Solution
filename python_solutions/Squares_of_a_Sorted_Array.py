# https://leetcode.com/problems/squares-of-a-sorted-array/
#Solving the above question
#Example input [-4,-1,0,3,10]
# OUTPUT : [0,1,9,16,100]
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

def sortedSquares(A):
    result = []
    for x in A:
        result.append(x*x)
    return sorted(result)

def sortedSqaures_list_comphrension(A):
    return sorted([x ** 2 for x in A])

if __name__ == '__main__':
    print(sortedSquares([-4,-1,0,3,10]))
    print(sortedSquares([-7,-3,2,3,11]))
