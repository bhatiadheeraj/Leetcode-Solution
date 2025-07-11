class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        bracket_key = {
            '{' : '}',
            '[' : ']',
            '(' : ')'
        }
        
        stack = []
        for index in range(len(s)):
            item = s[index]
            if item in bracket_key.keys():
                stack.append(item)
            else:
                if stack == []:
                    return False
                if bracket_key[stack.pop()] != item:
                    return False
        if len(stack) != 0:
            return False
        return True