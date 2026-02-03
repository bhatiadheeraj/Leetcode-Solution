from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1 
        countCharacters = Counter(s)

        res = 0

        for item, count in countCharacters.items():
            res += count // 2 * 2

        if res < len(s):
            res += 1
        
        return res

        