class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def fill(image: List[List[int]], sr: int, sc: int, orignalColor:int, color: int):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
                return
            
            if image[sr][sc] != originalColor:
                return
            
            image[sr][sc] = color

            fill(image, sr-1,sc,originalColor,color)
            fill(image, sr,sc+1,originalColor,color)
            fill(image, sr,sc-1,originalColor,color)
            fill(image, sr+1,sc,originalColor,color)

        originalColor = image[sr][sc]
        if originalColor == color:
            return image

        fill(image, sr,sc,originalColor,color)
        return image
