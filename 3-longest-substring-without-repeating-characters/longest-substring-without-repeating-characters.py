class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        res_set = set()
        max_length = 0 

        for right in range(len(s)):
            item = s[right]
            while item in res_set:
                res_set.remove(s[left])
                left+=1
            res_set.add(item)
            max_length = max(max_length, right  - left + 1)
        
        return max_length
