class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldcolor = image[sr][sc]
        if oldcolor == color:
            return image
        print(len(image[0]), len(image))
        self.fill(image, sr, sc, oldcolor, color)
        return image

    def fill(self,image, sr,sc,oldcolor,color):
        if sr >= 0 and sc >=0 and sr < len(image) and sc < len(image[0]) and image[sr][sc] == oldcolor:
            image[sr][sc] = color
            self.fill(image, sr+1, sc, oldcolor, color)
            self.fill(image, sr, sc+1, oldcolor, color)
            self.fill(image, sr-1, sc, oldcolor, color)
            self.fill(image, sr, sc-1, oldcolor, color)
        else:
            return
