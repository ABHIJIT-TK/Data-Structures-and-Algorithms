def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    if image[sr][sc] == newColor:
        return image

    def fill(image, r, c, targetColor, newColor):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != targetColor:
            return
        image[r][c] = newColor
        fill(image, r+1, c, targetColor, newColor)
        fill(image, r-1, c, targetColor, newColor)
        fill(image, r, c+1, targetColor, newColor)
        fill(image, r, c-1, targetColor, newColor)

    fill(image, sr, sc, image[sr][sc], newColor)
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

solution = floodFill(image, sr, sc, newColor)
for row in solution:
    print(row)
