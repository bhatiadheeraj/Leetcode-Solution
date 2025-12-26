class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for item in s:
            if item in brackets.keys():
                if len(stack) == 0:
                    return False
                if brackets[item] != stack.pop():
                    return False
            else:
                stack.append(item)
        if len(stack) > 0:
            return False

        return True