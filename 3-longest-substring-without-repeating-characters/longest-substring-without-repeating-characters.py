class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_tracker = set()

        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in set_tracker:
                set_tracker.remove(s[left])
                left += 1
            set_tracker.add(s[right])
        
            res = max(res, right - left + 1)

        return res
