# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
#Solving the above question
#Example Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
#EASY
def smallerNumbersThanCurrent(list_n):
    count = 0 
    returnList = []
    len_list = len(list_n)
    for x in list_n:
        for y in range(len_list):
            if (list_n[y] < x):
                count+=1
        returnList.append(count)
        count = 0 
    return returnList

if __name__ == '__main__':
    print(smallerNumbersThanCurrent([8,1,2,2,3]))