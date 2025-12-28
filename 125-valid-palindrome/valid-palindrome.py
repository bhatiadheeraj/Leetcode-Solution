class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        result = ""
        for char in s:
            if char.isalnum() == True:
                result += ""+char.lower()

        for index in range(0,int(len(result)/2)):
            if result[index] != result[len(result)- index - 1]:
                return False
        return True