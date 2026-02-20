class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == color:
            return image
        self.fill(image,sr,sc,oldColor, color)
        return image
    def fill(self, image, sr, sc,oldColor, newColor):
        if sr >= 0 and sr < len(image) and sc >=0 and sc < len(image[0]) and image[sr][sc] == oldColor:
            image[sr][sc] = newColor
            self.fill(image, sr+1, sc, oldColor, newColor)
            self.fill(image, sr-1, sc, oldColor, newColor)
            self.fill(image, sr, sc+1, oldColor, newColor)
            self.fill(image, sr, sc-1, oldColor, newColor)

