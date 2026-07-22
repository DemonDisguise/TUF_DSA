# Flood fill algorithm 
""" You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill. """


import sys
from collections import deque


def solve(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    original_color = image[sr][sc]
    
    if original_color == color:
        return image
    
    m, n = len(image), len(image[0])
    q = deque([(sr, sc)])
    image[sr][sc] = color
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    while q:
        row, col = q.popleft()
        
        for dr, dc in directions:
            nrow = row + dr
            ncol = col + dc
            
            if 0 <= nrow < m and 0 <= ncol < n and image[nrow][ncol] == original_color:
                image[nrow][ncol] = color
                q.append((nrow, ncol))
    
    return image

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    img = []
    for line in lines[:-1]:
        img.append(list(map(int, line.strip().split())))
    sr, sc, color = map(int, lines[-1].strip().split())
    res = solve(img, sr, sc, color)
    for row in res:
        print(*row)

# 1 1 1
# 1 1 0
# 1 0 1
# 1 1 2  