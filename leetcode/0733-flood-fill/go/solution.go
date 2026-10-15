package leetcode

func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	sourceColor := image[sr][sc]
	if sourceColor != color {
		dfs(image, sr, sc, sourceColor, color)
	}
	return image
}

func dfs(image [][]int, x int, y int, sourceColor int, newColor int) {
	if x < 0 || x >= len(image) || y < 0 || y >= len(image[0]) || image[x][y] != sourceColor {
		return
	}
	image[x][y] = newColor
	dfs(image, x-1, y, sourceColor, newColor)
	dfs(image, x+1, y, sourceColor, newColor)
	dfs(image, x, y-1, sourceColor, newColor)
	dfs(image, x, y+1, sourceColor, newColor)
}
