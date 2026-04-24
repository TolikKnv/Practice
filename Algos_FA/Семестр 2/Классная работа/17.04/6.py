# from functools import cache

maze = ["S----", "##---", "---##", "---#X"]


def labirint(road, row, col, visited=set()):
    if row < 0 or col < 0 or row >= len(road) or col >= len(road[0]):
        return False

    if road[row][col] == "#" or (row, col) in visited:
        return False
    if road[row][col] == "X":
        return True
    visited.add((row, col))

    return (
        labirint(road, row - 1, col, visited) or
        labirint(road, row + 1, col, visited) or
        labirint(road, row, col - 1, visited) or
        labirint(road, row, col + 1, visited)
    )

print(labirint(maze, 0, 0))