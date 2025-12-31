class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for item in s:
            #opening bracket to stack
            if brackets.get(str(item), 0) == 0:
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                front = stack.pop()
                if brackets.get(str(item), 0) != str(front):
                    return False
        if len(stack) > 0:
            return False
        
        return True
