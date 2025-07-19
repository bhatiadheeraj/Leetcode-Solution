class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        s_char_count = {}
        t_char_count = {}

        for index in range(0,len(s)):
            char_s = s[index]
            char_t = t[index]

            if t_char_count.get(char_t, None) == None:
                t_char_count[char_t] = 1
            else:
                t_char_count[char_t] +=1

            if s_char_count.get(char_s,None) == None:
                s_char_count[char_s] = 1
            else:
                s_char_count[char_s] +=1

        for key in s_char_count.keys():
            if s_char_count.get(key) != None and t_char_count.get(key) !=None and t_char_count.get(key) == s_char_count.get(key):
                print("ok")
            else:
                return False
        
        return True