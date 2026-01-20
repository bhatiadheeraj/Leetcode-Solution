from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)

        count = 0

        for item in char_count.values():
            count += item // 2 * 2

        if count < len(s) : 
            count += 1

        return count