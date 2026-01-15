class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1, 1, 2]


        for index in range(3, n+1):
            print(index, ways[index -1 ], ways[index-2])
            ways.append(ways[index - 1] + ways[index - 2])
        return ways[n]
        