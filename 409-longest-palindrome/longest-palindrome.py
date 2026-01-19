from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0 
        char_count = Counter(s)
        for key, value in char_count.items():
            count += value // 2 * 2
        
        if count < len(s):
            count += 1
        
        return count
