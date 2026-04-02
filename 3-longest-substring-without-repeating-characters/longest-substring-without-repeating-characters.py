class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_set = set()
        left = 0 
        maxRes= 0 

        for right in range(len(s)):
            item = s[right]
            while item in res_set:
                res_set.remove(s[left])
                left+=1
            res_set.add(item)
            maxRes = max(maxRes, right - left + 1)
        
        return maxRes