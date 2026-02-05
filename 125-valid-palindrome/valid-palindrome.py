class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for char in s:
            if char.isalnum() == True:
                res = res + ""+char.lower()

        for i in range(0, int(len(res)/2)):
            if res[i] != res[len(res) -1 - i] :
                return False

        return True
            
