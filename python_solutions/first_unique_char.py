https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # if len(s) ==1 : return 0
        # for i in range(0,len(s)):
        #     copy = list(s)
        #     if copy.count(s[i]) < 2:
        #         return i
        diction = Counter(s).items()
        for j,k in diction:
            if(k == 1):
                return s.index(j)
        return -1
