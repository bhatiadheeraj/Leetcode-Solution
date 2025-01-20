class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_length = 0

        for index,value in enumerate(s):
            print(index,value)
            if value in char_map and char_map[value] >= left:
                left = char_map[value] + 1
            char_map[value] = index #index index
            max_length = max(max_length, index - left + 1)
        return max_length
        