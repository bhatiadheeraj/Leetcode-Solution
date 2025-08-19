class Solution:
    def climbStairs(self, n: int) -> int:
        arr = []
        arr.append(0)
        arr.append(1)
        arr.append(2)

        for index in range(3, n+1):
            arr.append(arr[index-1] + arr[index - 2])
        
        return arr[n]