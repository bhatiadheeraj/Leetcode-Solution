class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_to_val = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        sum = 0
        s = s.replace('IV', 'IIII') \
             .replace('IX', 'VIIII') \
             .replace('XL', 'XXXX') \
             .replace('XC', 'LXXXX') \
             .replace('CD', 'CCCC') \
             .replace('CM', 'DCCCC')

        for index,char in enumerate(list(s)):
            sum += symbol_to_val[char]
        
        return sum