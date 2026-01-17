from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_character = Counter(s)
        total = 0

        for char,count in count_character.items(): 
            total += count // 2 * 2
        
        if total < len(s):
            total += 1
    
        return total