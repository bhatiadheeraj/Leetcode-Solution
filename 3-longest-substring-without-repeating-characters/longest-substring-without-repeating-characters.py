class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set() #empty a

        left = 0 
        res = 0 #1

        for right in range(len(s)): #0
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right-left+1) #1
        
        return res