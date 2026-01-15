from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1: 
            return 1
        charCount = Counter(s)
        print(charCount)

        count = 0

        for key,value in charCount.items():
            print(value)
            if value % 2 == 0:
                count += value
            else:
                count += value - 1
        if count < len(s) : count += 1
        return count

        
        


        