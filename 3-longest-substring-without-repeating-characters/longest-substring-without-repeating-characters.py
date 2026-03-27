class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        result_set = set()
        maxRes = 0

        for right in range(len(s)):
            item = s[right]
            while item in result_set:
                result_set.remove(s[left])
                left+=1
            result_set.add(item)
            maxRes = max(maxRes, right - left + 1)
        
        return maxRes
            