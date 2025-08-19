class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        length = 0
        odd_found = False
        
        # Add pairs to length
        for count in char_count.values():
            length += (count // 2) * 2
            if count % 2 == 1:
                odd_found = True
        
        # If there’s any odd, we can put one in the middle
        if odd_found:
            length += 1
        
        return length