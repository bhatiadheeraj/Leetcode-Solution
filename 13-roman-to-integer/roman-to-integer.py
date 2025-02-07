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

        total = 0
        prev = 0
        #IV -> #VI
        for index,char in enumerate(reversed(list(s))):
            char_val = symbol_to_val[char]
            if char_val >= prev :
                total += char_val
            else:
                total -= char_val
            prev = char_val
        return total