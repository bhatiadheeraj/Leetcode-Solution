class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
    
        set_result = set()
        max_len = 0

        for right in range(len(s)):
            while s[right] in set_result:
                set_result.remove(s[left])
                left+=1
            
            set_result.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
