class Solution:
    def isValid(self, s: str) -> bool:
        dict_bracket = {
            '}' : '{',
            ']' : '[', 
            ')' : '('
        }

        stack = []

        for char in s:
            if dict_bracket.get(char, 0) != 0 and len(stack) > 0:
                val_at_front = stack.pop()
                if val_at_front != dict_bracket.get(char,0):
                    return False
            else:
                stack.append(char)
        if len(stack) != 0:
            return False
        return True