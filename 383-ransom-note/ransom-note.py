class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_to_count_ransomNote = {}
        char_to_count_magazine = {}
        
        for item in magazine:
            if char_to_count_magazine.get(item,0):
                char_to_count_magazine[item] += 1
            else :
                char_to_count_magazine[item] = 1
        
        for item in ransomNote:
            if char_to_count_ransomNote.get(item,0):
                char_to_count_ransomNote[item] += 1
            else :
                char_to_count_ransomNote[item] = 1
        
        for key in char_to_count_ransomNote.keys():
            if char_to_count_magazine.get(key,0) < char_to_count_ransomNote.get(key,0):
                return False
        
        return True