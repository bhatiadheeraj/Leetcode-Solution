class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_set = set()
        maxResult = 0

        left = 0 

        for right in range(0, len(s)):
            item = s[right]

            while item in res_set:
                res_set.remove(s[left])
                left += 1
            res_set.add(item)
            maxResult = max(maxResult, right - left + 1)

        return maxResult 