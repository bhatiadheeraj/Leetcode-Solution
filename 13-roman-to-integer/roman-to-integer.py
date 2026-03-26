class Solution:
    def romanToInt(self, s: str) -> int:
        SYMBOL_TO_VAL = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        result = 0
        last_item = 0
        for index, item in enumerate(s): # 1000 1100 2000 2010 2111
            value = SYMBOL_TO_VAL[item]
            if last_item < value:
                result -= last_item 
                result += value-last_item
            else:
                result += value
            last_item = value
        return result
