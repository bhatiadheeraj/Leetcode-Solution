from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterMagazine = Counter(magazine)

        for item in ransomNote:
            if counterMagazine.get(item, -1) <= 0:
                return False
            counterMagazine[item] -= 1
        
        return True


