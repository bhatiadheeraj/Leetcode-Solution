class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
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
        for item in s:
            if roman_to_int.get(last_item,0) < roman_to_int.get(item,0):
                result -= 2* roman_to_int.get(last_item,0)
            result += roman_to_int.get(item,0)
            last_item = item
        
        return result