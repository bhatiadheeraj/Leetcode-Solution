class Solution:
    def isValid(self, s: str) -> bool:
        dict_bracket = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        stack = []

        for char in s:
            if dict_bracket.get(char, 0) != 0 and len(stack):
                closing_bracket = stack.pop()
                if closing_bracket != dict_bracket.get(char, 0):
                    return False
            else:
                stack.append(char)
        
        if len(stack):
            return False
        
        return True