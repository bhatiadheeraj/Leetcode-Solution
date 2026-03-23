class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        res = set()
        maxResult = 0
        for right in range(len(s)):
            item = s[right]
            while item in res:
                res.remove(s[left])
                left +=1
            res.add(item)
            maxResult = max(maxResult, right - left + 1)

        return maxResult