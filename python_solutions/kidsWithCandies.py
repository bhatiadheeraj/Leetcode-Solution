# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
#Solving the above question
#Example input candies = [2,3,5,1,3], extraCandies = 3
# OUTPUT : [true,true,true,false,true]

def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    greatestno = max(candies)
    returnList = []
    for x in candies:
        if(x + extraCandies >= greatestno):
            returnList.append(True)
        else:
            returnList.append(False)
    return returnList


if __name__ == '__main__':
        print(kidsWithCandies([2,3,5,1,3],3))