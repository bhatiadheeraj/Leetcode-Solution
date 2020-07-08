# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
#Solving the above question
#Example input num = 14
# OUTPUT : 6

def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """
    steps = 0
    number = num
    while(number != 0):
        if(number %2 == 0):
            steps +=1
            number = number/2
        else:
            steps +=1
            number = (number-1)
    return steps

if __name__ == '__main__':
    print(numberOfSteps(14))
