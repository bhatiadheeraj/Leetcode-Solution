from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_mag = Counter(magazine)

        for index in range(0, len(ransomNote)):
            char = ransomNote[index]
            if count_mag.get(char, 0) >0:
                count_mag[char] -= 1
            else:
                return False
        
        return True