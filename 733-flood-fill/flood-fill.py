class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            self.fill(image, sr,sc,image[sr][sc], color)
        return image

    def fill(self, image: List[List[int]], sr: int, sc: int, oldcolor: int, newColor: int):
        if sr >= 0 and sc >= 0 and sr < len(image) and sc < len(image[0]) and image[sr][sc] == oldcolor:
            image[sr][sc] =newColor
            self.fill(image, sr+1,sc, oldcolor, newColor)
            self.fill(image, sr-1,sc,oldcolor, newColor)
            self.fill(image, sr,sc+1,oldcolor, newColor)
            self.fill(image, sr,sc-1,oldcolor, newColor)