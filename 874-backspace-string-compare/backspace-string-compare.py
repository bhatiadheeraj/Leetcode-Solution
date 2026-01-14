class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for item in s:
            if item == '#' and len(stack_s): 
                stack_s.pop()
            if item !='#':
                stack_s.append(item)

        for item in t:
            if item == '#' and len(stack_t):
                stack_t.pop()
            if item != '#':
                stack_t.append(item)
        
        print(stack_s,stack_t)
        return stack_s == stack_t