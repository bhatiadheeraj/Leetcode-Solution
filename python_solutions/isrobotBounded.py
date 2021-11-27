https://leetcode.com/problems/robot-bounded-in-circle/submissions/
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = {
            "N" : {
                "R" : "E",
                "L" : "W",
            },
            "S" : {
                "R" : "W",
                "L" : "E",
            },
            "E" : {
                "R" : "S",
                "L" : "N",
            },
            "W": {
                "R" : "N",
                "L": "S"
            }    
        }
        initDirection = "N"

        cx = 0
        cy = 0
        
        for x in instructions:
            if x == 'G':
                if initDirection == "N":
                    cx+=1
                if initDirection == "S":
                    cx -= 1
                if initDirection == "W":
                    cy += 1
                if initDirection == "E":
                    cy -=1
            else:
                initDirection = directions[initDirection][x]

        return (cx == 0 and cy == 0) or initDirection != 'N'
