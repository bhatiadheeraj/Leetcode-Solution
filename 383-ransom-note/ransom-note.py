class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charCount_magazine = {}
        for item in magazine:
            if charCount_magazine.get(item, 0) == 0 :
                charCount_magazine[item] = 1
            else:
                charCount_magazine[item] +=1
        
        charCount_ransomNote = {}

        for item in ransomNote:
            if charCount_ransomNote.get(item,0) == 0:
                charCount_ransomNote[item] = 1
            else:
                charCount_ransomNote[item] += 1
            if charCount_ransomNote[item] > charCount_magazine.get(item, 0):
                return False
        

        return True


        