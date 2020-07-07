# https://leetcode.com/problems/shuffle-the-array/
#Solving the above question
#Example input nums = [2,5,1,3,4,7], n = 3
# OUTPUT : [2,3,5,4,1,7]
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]

def shuffle(nums, n):
    result = []
    div = int(len(nums)+1/n)
    for x in range(int(len(nums)/2)):
        result.append(nums[x])
        result.append(nums[x+n])
    return result



if __name__ == '__main__':
        print(shuffle([2,5,1,3,4,7],3))
        print(shuffle([1,1,2,2],2))

