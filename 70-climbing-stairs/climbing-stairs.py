class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 1, 2]
        
        for index in range(3, n+1):
            steps.append(steps[index-1]+steps[index-2])
        
        return steps[n]