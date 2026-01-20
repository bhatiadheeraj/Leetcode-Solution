from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #each letter in magazine only be used once in ransomNote
        if len(magazine) < len(ransomNote):
            return False
        # each unique char in magazine should be present atleast equally or more than ransomeNote

        count_char_ransom_note = Counter(ransomNote)
        count_char_magazine = Counter(magazine)
        
        for key,val in count_char_ransom_note.items(): 
            if count_char_magazine.get(key, 0) < val:
                return False
        return True
        