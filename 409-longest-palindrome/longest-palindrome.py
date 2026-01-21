from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0 

        for item in Counter(s).values():
            count += item // 2 * 2 
        
        if count < len(s):
            count +=1
        
        return count
        