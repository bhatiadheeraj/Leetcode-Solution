class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        if s[0] == ']' or s[0] == '}' or s[0] == ')':
            return False

        map_bracket = {
            '[' : ']',
            '{' : '}',
            '(' : ')' 
        }

        stack = []

        #s = '{}'

        for item in s:
            if item in map_bracket.keys():
                stack.append(item)
            if item in map_bracket.values():
                if len(stack) !=0:
                    front_of_list = stack.pop()
                    if map_bracket[front_of_list] != item:
                            return False
                else:
                    return False
        
        return len(stack) == 0       