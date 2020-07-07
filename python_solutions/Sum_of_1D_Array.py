# https://leetcode.com/problems/running-sum-of-1d-array/
#Solving the above question
#Example input [1,2,3,4]
# OUTPUT : [1,3,6,10]


def runningSum(nums):
    output = []
    output_hold = 0
    for x in nums:
        output_hold = output_hold + x
        output.append(output_hold)
    return output

if __name__ == '__main__':
    print(runningSum([1,2,3,4]))

# Runtime : 36 ms
# Memory : 12.8 MB
