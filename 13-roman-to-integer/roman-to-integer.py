class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        num = 0
        last_char = ''
        for char in s:
            num += symbol_value.get(char, 0)
            if last_char and symbol_value[char] > symbol_value[last_char]:
                num -= 2 * symbol_value[last_char]
            last_char = char
        
        return num
