class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 !=0 :
            return False

        stack = []

        dict_bracket = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for bracket in s:
            if dict_bracket.get(bracket, 0) != 0 and len(stack) >  0:
                stack_top = stack.pop()
                if dict_bracket[bracket] != stack_top:
                #if its a closing bracket then the top of stack should have its open bracket
                #stack 
                    print("here", dict_bracket[bracket], stack_top)
                    return False
            else:
                stack.append(bracket)
        
        if len(stack) !=0 : 
            return False
        
        return True