class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 # 0 1
        result_set = set() # # p w w -> p w
        res_length = 0 # # 1 2 

        for right in range(len(s)):
            item = s[right]
            while item in result_set:
                result_set.remove(s[left])
                left += 1
            result_set.add(item)
            res_length = max(res_length, right-left + 1)

        return res_length