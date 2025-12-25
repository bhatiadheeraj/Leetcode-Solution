class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <=1:
            return False
        
        stack = []
        brackets = {
        ")" : "(",
        "}": "{",
        "]": "["
        }
        for item in s:
            if item in brackets.values():
                stack.append(item)
            if item in brackets.keys():
                if len(stack) >= 1 and stack[-1] == brackets.get(""+item,None):
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
    